# UWE Map - Interactive County Analysis Tool

An interactive map visualization tool for analyzing counties across multiple dimensions: Real Estate, Wood & Energy, Philanthropic Support, and City & County Climate Goals.

## Features

- **Interactive Map**: Explore US counties with dynamic scoring
- **Multiple Dimensions**: 
  - Real Estate factors (land cost, brownfield density, exit rates)
  - Wood & Energy infrastructure (mills, energy demand, labor)
  - Philanthropic support (capacity, funder presence, nonprofit ecosystem)
  - City & County Climate goals (CO2 emissions, green infrastructure, ACEEE scores)
- **Collapsible Controls**: Organize dimensions with dropdown menus
- **Customizable Weights**: Adjust sub-dimension weights with sliders
- **Combined Scoring**: Scores add together for cumulative visualization


## File Structure

```
uwe-map/
├── index.html                    # Main HTML file
├── county_core.geojson          # County data with all merged scores
├── Real Estate/
│   ├── real_estate.json        # Real Estate config
│   └── brownfieldcoords.geojson # Brownfield points
├── WoodEnergy/
│   ├── wood_energy.json         # Wood & Energy config
│   └── mills_points.geojson     # Mill locations
├── Philanthropic/
│   └── philanthropic.json       # Philanthropic config
└── City & County Climate/
    └── climate.json             # Climate config
```

## Local Development

To run locally:

```bash
cd uwe-map
python3 -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## Notes

- All data is loaded from local GeoJSON and JSON files
- The map uses MapLibre GL for rendering
- No backend required - fully client-side
- Works offline once files are loaded

