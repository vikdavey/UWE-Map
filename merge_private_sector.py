import json
import sys

# Increase recursion limit for large files
sys.setrecursionlimit(50000)

# Paths
PRIVATE_SECTOR_GEOJSON = "PrivateSector.geojson"
COUNTY_GEOJSON = "../county_core.geojson"
OUTPUT_GEOJSON = "../county_core.geojson"

# Private Sector field names
PRIVATE_SECTOR_FIELDS = [
    "Private Partner Score - final_joined_output (4)_S_Dim1_Size",
    "Private Partner Score - final_joined_output (4)_S_Dim2_Growth"
]

print("Loading private sector data...")
with open(PRIVATE_SECTOR_GEOJSON, "r", encoding="utf-8") as f:
    private_sector_data = json.load(f)

# Build lookup: GEOID -> properties
private_sector_lookup = {}
for feature in private_sector_data.get("features", []):
    props = feature.get("properties", {})
    geoid = props.get("GEOID")
    if geoid:
        private_sector_lookup[geoid] = props

print(f"Loaded {len(private_sector_lookup)} private sector records")

print("Loading county data...")
with open(COUNTY_GEOJSON, "r", encoding="utf-8") as f:
    county_data = json.load(f)

matched = 0
missing = 0

print("Merging private sector data...")
for feature in county_data.get("features", []):
    props = feature.get("properties", {})
    geoid = props.get("GEOID") or props.get("geoid")
    
    if not geoid:
        missing += 1
        # Fill with None if no GEOID
        for field in PRIVATE_SECTOR_FIELDS:
            props[field] = None
        continue
    
    private_sector_props = private_sector_lookup.get(geoid)
    if private_sector_props:
        matched += 1
        # Copy private sector fields
        for field in PRIVATE_SECTOR_FIELDS:
            val = private_sector_props.get(field)
            if val is None or val == "":
                props[field] = None
            elif isinstance(val, str):
                try:
                    props[field] = float(val)
                except (ValueError, TypeError):
                    props[field] = None
            else:
                props[field] = float(val) if val is not None else None
    else:
        missing += 1
        # Fill with None if no match
        for field in PRIVATE_SECTOR_FIELDS:
            props[field] = None

print(f"Matched {matched} counties, missing {missing}")

print(f"Saving merged data to {OUTPUT_GEOJSON}...")
with open(OUTPUT_GEOJSON, "w", encoding="utf-8") as f:
    json.dump(county_data, f)

print("Done! Private sector data has been merged into county_core.geojson")

