#!/bin/bash

echo "=== UWE Map Deployment Checklist ==="
echo ""

# Check for required files
echo "Checking required files..."
REQUIRED_FILES=(
  "index.html"
  "county_core.geojson"
  "Real Estate/real_estate.json"
  "Real Estate/brownfieldcoords.geojson"
  "WoodEnergy/wood_energy.json"
  "WoodEnergy/mills_points.geojson"
  "Philanthropic/philanthropic.json"
  "City & County Climate/climate.json"
)

MISSING=0
for file in "${REQUIRED_FILES[@]}"; do
  if [ -f "$file" ]; then
    echo "✓ $file"
  else
    echo "✗ MISSING: $file"
    MISSING=$((MISSING + 1))
  fi
done

echo ""
if [ $MISSING -eq 0 ]; then
  echo "✓ All required files present!"
  echo ""
  echo "Your site is ready to deploy!"
  echo ""
  echo "Quick deploy options:"
  echo "1. GitHub Pages: See DEPLOY.md"
  echo "2. Netlify: Drag this folder to app.netlify.com"
  echo "3. Vercel: Run 'vercel' in this directory"
else
  echo "✗ Missing $MISSING file(s). Please ensure all files are present before deploying."
fi

echo ""
echo "File sizes:"
du -sh county_core.geojson 2>/dev/null || echo "county_core.geojson not found"
du -sh index.html 2>/dev/null || echo "index.html not found"

