# Quick Deployment Guide

## For GitHub Pages

1. **Create a GitHub repository** (if you haven't already)
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/uwe-map.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**
   - Go to your repository on GitHub
   - Click Settings → Pages
   - Under "Source", select your branch (main/master)
   - Select "/ (root)" folder
   - Click Save
   - Your site will be at: `https://yourusername.github.io/uwe-map`

## For Netlify (Easiest)

1. Go to [app.netlify.com](https://app.netlify.com)
2. Sign up/Login
3. Click "Add new site" → "Deploy manually"
4. Drag the entire `uwe-map` folder into the browser
5. Done! You'll get a URL like `https://random-name-123.netlify.app`

## For Vercel

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Deploy:
   ```bash
   cd uwe-map
   vercel
   ```

3. Follow the prompts - your site will be live in seconds!

## Important Notes

- **All files must be included**: Make sure `county_core.geojson` and all other data files are committed
- **File paths**: The site uses relative paths, so it should work on any hosting service
- **CORS**: If hosting on a different domain, you may need to configure CORS headers (most hosting services handle this automatically)

## Testing Before Deployment

1. Run locally: `python3 -m http.server 8000`
2. Open `http://localhost:8000`
3. Check browser console (F12) for any errors
4. Verify all data loads correctly
5. Test all dimension controls

Once everything works locally, you're ready to deploy!

