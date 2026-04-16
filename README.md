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

## Deployment Options

### Option 1: GitHub Pages (Free & Easy)

1. Create a new GitHub repository
2. Push all files to the repository
3. Go to Settings → Pages
4. Select your branch (usually `main` or `master`)
5. Select `/ (root)` as the source
6. Your site will be available at `https://yourusername.github.io/repository-name`

**Important**: Make sure to include all these files:
- `index.html`
- `county_core.geojson`
- All JSON config files in subdirectories
- All GeoJSON data files

### Option 2: Netlify (Free & Easy)

1. Go to [netlify.com](https://netlify.com)
2. Sign up/login
3. Drag and drop the entire `uwe-map` folder onto Netlify
4. Your site will be live instantly with a URL like `https://random-name.netlify.app`

### Option 3: Vercel (Free & Easy)

1. Install Vercel CLI: `npm i -g vercel`
2. In the project directory, run: `vercel`
3. Follow the prompts
4. Your site will be deployed

### Option 4: Any Static Hosting Service

This is a static site (HTML, CSS, JavaScript), so it works on:
- AWS S3 + CloudFront
- Google Cloud Storage
- Azure Static Web Apps
- Any web hosting service that supports static files

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

## License

[Add your license here]

