# African American Newspapers Interactive Map

An interactive web-based map showcasing 50 African American newspapers across the United States - including 20 currently active publications and 30 historical newspapers that have ceased publication.

## Overview

This project creates an interactive dashboard that displays the geographic locations of prominent African American newspapers throughout the United States. The map includes both historically significant newspapers and currently active publications, highlighting their important role in journalism, community engagement, and documenting African American history from 1827 to the present day.

## Features

- **Interactive Map**: Click on markers to view detailed information about each newspaper
- **Timeline Slider**: Filter newspapers by year (1827-2025) to see which publications were active at any point in history
- **Color-Coded Markers**: Green markers for active newspapers, gray markers for ceased publications
- **Circulation Dates**: View complete publication history with founding and cessation dates
- **Sidebar Navigation**: Browse and select newspapers from a searchable list with years
- **Responsive Design**: Works on desktop and mobile devices
- **City-Level Views**: Zoom in to see each newspaper's location in detail
- **Historical Context**: Spanning from 1827 (Freedom's Journal) to present day publications
- **Dynamic Filtering**: Real-time updates showing active newspaper count for selected year

## Files

- `index.html` - Main interactive map (pure JavaScript - ready for GitHub Pages deployment)
- `periodicals.json` - Geolocation data for all 50 newspapers (20 active, 30 historical)
- `create_map.py` - [DEPRECATED] Python script (not needed - kept for reference only)
- `claude.md` - OpenStreetMap data extraction planning document

## Newspapers Included

The map features 50 African American newspapers across the United States:

### Active Newspapers (20)
Including The Philadelphia Tribune (1884-), The Chicago Defender (1905-), The Amsterdam News (1909-), The Afro-American (1892-), Los Angeles Sentinel (1933-), and 15 others currently in circulation.

### Historical Newspapers (30)
Including pioneering publications like:
- **Freedom's Journal** (1827-1829) - The first African American newspaper in the United States
- **The North Star** (1847-1851) - Founded by Frederick Douglass
- **The California Eagle** (1879-1964) - Los Angeles
- **The New York Age** (1887-1960)
- **The Cleveland Gazette** (1883-1945)
- **The Boston Guardian** (1901-1957)
- **The Chicago Whip** (1919-1939)
- And 23 other historically significant publications that documented African American life and the civil rights movement

The newspapers span across major cities including New York, Chicago, Los Angeles, Philadelphia, Detroit, Atlanta, Houston, Baltimore, Washington DC, and many others, representing diverse regions and communities throughout American history.

## Technology Stack

- **JavaScript/HTML/CSS**: Frontend interface (pure client-side, no build process required)
- **Leaflet.js**: Interactive mapping library
- **OpenStreetMap**: Map tiles and data
- **Font Awesome**: Icons
- **JSON**: Static data storage

## Deployment

This project is designed for deployment on GitHub Pages:

1. Push all files to your GitHub repository
2. Go to repository Settings → Pages
3. Select the branch containing the files
4. The site will be available at: `https://username.github.io/repository-name/`

## Local Development

No build process required! Simply:

1. Open `index.html` in your web browser to view the map locally
2. To add or update newspapers, edit `periodicals.json`
3. Refresh the browser to see changes

The map loads data dynamically from `periodicals.json` using JavaScript.

## Using the Timeline Filter

The interactive timeline slider allows you to explore which newspapers were active at any point in American history:

1. **Drag the slider** to select a specific year between 1827 and 2025
2. **Watch the map update** in real-time to show only newspapers that were in circulation during that year
3. **View the counter** to see how many newspapers were active in the selected year
4. **Click "Show All Years"** to reset the filter and display all 50 newspapers

### Example Timeline Queries

- **1847**: See Frederick Douglass's *The North Star* alongside other early publications
- **1900**: View newspapers active at the turn of the century
- **1950**: Explore newspapers during the Civil Rights movement
- **1990**: See which publications were still in print in the late 20th century
- **2025**: Current active publications only

The timeline provides a unique perspective on the evolution of African American journalism across nearly two centuries.

## Data Sources

- Newspaper locations: Publicly available address information
- Geocoding: OpenStreetMap Nominatim
- Map tiles: OpenStreetMap contributors

## License

This project uses OpenStreetMap data, which is © OpenStreetMap contributors and available under the Open Database License (ODbL).

## Contributing

To add more newspapers or update information:

1. Edit `periodicals.json` with the new data:
   - Required fields: name, city, state, address, latitude, longitude, founded_year, status
   - Optional fields: ceased_year (for historical newspapers), website (for active newspapers)
   - Status should be either "active" or "ceased"
2. Test by opening `index.html` in your browser
3. Submit a pull request

## Acknowledgments

This project honors the legacy of African American newspapers and their vital role in documenting and shaping African American history, culture, and civil rights movements in the United States.
