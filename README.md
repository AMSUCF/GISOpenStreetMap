# African American Newspapers Interactive Map

An interactive web-based map showcasing 20 historic and active African American newspapers across the United States.

## Overview

This project creates an interactive dashboard that displays the geographic locations of prominent African American newspapers throughout the United States. The map includes both historically significant and currently active publications, highlighting their important role in journalism and community engagement.

## Features

- **Interactive Map**: Click on markers to view detailed information about each newspaper
- **Sidebar Navigation**: Browse and select newspapers from a searchable list
- **Responsive Design**: Works on desktop and mobile devices
- **City-Level Views**: Zoom in to see each newspaper's location in detail
- **Historical Context**: View founding years and publication status

## Files

- `index.html` - Main interactive map (pure JavaScript - ready for GitHub Pages deployment)
- `periodicals.json` - Geolocation data for all 20 newspapers
- `create_map.py` - [DEPRECATED] Python script (not needed - kept for reference only)
- `claude.md` - OpenStreetMap data extraction planning document

## Newspapers Included

The map features 20 African American newspapers including:

1. The Philadelphia Tribune (1884) - Philadelphia, PA
2. The Indianapolis Recorder (1895) - Indianapolis, IN
3. The Afro-American (1892) - Baltimore, MD
4. The Chicago Defender (1905) - Chicago, IL
5. The Pittsburgh Courier (1907) - Pittsburgh, PA
6. The Amsterdam News (1909) - New York, NY
7. The Miami Times (1923) - Miami, FL
8. The Atlanta Daily World (1928) - Atlanta, GA
9. The Cleveland Call and Post (1928) - Cleveland, OH
10. The St. Louis American (1928) - St. Louis, MO
11. The Houston Defender (1930) - Houston, TX
12. Los Angeles Sentinel (1933) - Los Angeles, CA
13. The Michigan Chronicle (1936) - Detroit, MI
14. The Memphis Tri-State Defender (1951) - Memphis, TN
15. The Sacramento Observer (1962) - Sacramento, CA
16. The Washington Informer (1964) - Washington, DC
17. The New Orleans Data News Weekly (1966) - New Orleans, LA
18. The Seattle Medium (1970) - Seattle, WA
19. The Charlotte Post (1878) - Charlotte, NC
20. The Dallas Examiner (1986) - Dallas, TX

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

## Data Sources

- Newspaper locations: Publicly available address information
- Geocoding: OpenStreetMap Nominatim
- Map tiles: OpenStreetMap contributors

## License

This project uses OpenStreetMap data, which is © OpenStreetMap contributors and available under the Open Database License (ODbL).

## Contributing

To add more newspapers or update information:

1. Edit `periodicals.json` with the new data (include name, city, state, address, latitude, longitude, founded_year, status, website)
2. Test by opening `index.html` in your browser
3. Submit a pull request

## Acknowledgments

This project honors the legacy of African American newspapers and their vital role in documenting and shaping African American history, culture, and civil rights movements in the United States.
