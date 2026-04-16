import json

# Paths
PHILANTHROPIC_GEOJSON = "philanthropic-scores.geojson"
COUNTY_GEOJSON = "../county_core.geojson"
OUTPUT_GEOJSON = "../county_core.geojson"

# Philanthropic field names
PHILANTHROPIC_FIELDS = [
    "Philanthropic Support - Sheet1 (1)_Total Philanthropic Capacity",
    "Philanthropic Support - Sheet1 (1)_Aligned Funder Presence",
    "Philanthropic Support - Sheet1 (1)_Aligned Nonprofit Ecosystem"
]

print("Loading philanthropic data...")
with open(PHILANTHROPIC_GEOJSON, "r") as f:
    philanthropic_data = json.load(f)

# Build lookup: GEOID -> properties
philanthropic_lookup = {}
for feature in philanthropic_data.get("features", []):
    props = feature.get("properties", {})
    geoid = props.get("GEOID")
    if geoid:
        philanthropic_lookup[geoid] = props

print(f"Loaded {len(philanthropic_lookup)} philanthropic records")

print("Loading county data...")
with open(COUNTY_GEOJSON, "r") as f:
    county_data = json.load(f)

matched = 0
missing = 0

print("Merging philanthropic data...")
for feature in county_data.get("features", []):
    props = feature.get("properties", {})
    geoid = props.get("GEOID") or props.get("geoid")
    
    if not geoid:
        missing += 1
        # Fill with None if no GEOID
        for field in PHILANTHROPIC_FIELDS:
            props[field] = None
        continue
    
    philanthropic_props = philanthropic_lookup.get(geoid)
    if philanthropic_props:
        matched += 1
        # Copy philanthropic fields
        for field in PHILANTHROPIC_FIELDS:
            val = philanthropic_props.get(field)
            # Convert string numbers like "0.00E+00" to float
            if val is None or val == "":
                props[field] = None
            elif isinstance(val, str):
                try:
                    # Handle scientific notation
                    if "E" in val.upper() or "e" in val:
                        props[field] = float(val)
                    else:
                        props[field] = float(val)
                except (ValueError, TypeError):
                    props[field] = None
            else:
                props[field] = float(val) if val is not None else None
    else:
        missing += 1
        # Fill with None if no match
        for field in PHILANTHROPIC_FIELDS:
            props[field] = None

print(f"Matched {matched} counties, missing {missing}")

print(f"Saving merged data to {OUTPUT_GEOJSON}...")
with open(OUTPUT_GEOJSON, "w") as f:
    json.dump(county_data, f)

print("Done! Philanthropic data has been merged into county_core.geojson")

