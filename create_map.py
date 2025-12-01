#!/usr/bin/env python3
"""
Generate an interactive map of African American newspapers across the United States.
This script creates a self-contained HTML file suitable for deployment on GitHub Pages.
"""

import json
import folium
from folium import plugins

def load_periodicals_data(json_file='periodicals.json'):
    """Load newspaper data from JSON file."""
    with open(json_file, 'r') as f:
        return json.load(f)

def create_custom_icon(color='red'):
    """Create a custom marker icon."""
    return folium.Icon(
        color=color,
        icon='newspaper-o',
        prefix='fa'
    )

def create_newspaper_map(periodicals):
    """Create the main Folium map with all newspapers."""

    # Center map on continental US
    m = folium.Map(
        location=[39.8283, -98.5795],
        zoom_start=4,
        tiles='OpenStreetMap',
        attr='OpenStreetMap'
    )

    # Add each newspaper as a marker
    for newspaper in periodicals:
        # Create popup content with newspaper details
        popup_html = f"""
        <div style="font-family: Arial, sans-serif; width: 250px;">
            <h4 style="margin: 0 0 10px 0; color: #2c3e50;">{newspaper['name']}</h4>
            <p style="margin: 5px 0;"><strong>Location:</strong> {newspaper['city']}, {newspaper['state']}</p>
            <p style="margin: 5px 0;"><strong>Founded:</strong> {newspaper['founded_year']}</p>
            <p style="margin: 5px 0;"><strong>Status:</strong> {newspaper['status'].title()}</p>
            <p style="margin: 5px 0;">
                <a href="{newspaper['website']}" target="_blank" style="color: #3498db;">Visit Website</a>
            </p>
        </div>
        """

        # Add marker with custom icon
        folium.Marker(
            location=[newspaper['latitude'], newspaper['longitude']],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=newspaper['name'],
            icon=create_custom_icon('darkred')
        ).add_to(m)

    return m

def inject_dashboard_html(map_obj, periodicals):
    """Inject custom HTML, CSS, and JavaScript for dashboard functionality."""

    # Create sidebar HTML with list of newspapers
    newspapers_list = ""
    for i, newspaper in enumerate(sorted(periodicals, key=lambda x: x['name'])):
        newspapers_list += f"""
        <div class="newspaper-item" onclick="flyToLocation({newspaper['latitude']}, {newspaper['longitude']}, '{newspaper['name']}')">
            <div class="newspaper-name">{newspaper['name']}</div>
            <div class="newspaper-location">{newspaper['city']}, {newspaper['state']}</div>
        </div>
        """

    custom_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>African American Newspapers in the United States</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
            body {{
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}

            .header {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 20px 30px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}

            .header h1 {{
                margin: 0;
                font-size: 28px;
                font-weight: 600;
            }}

            .header p {{
                margin: 5px 0 0 0;
                font-size: 14px;
                opacity: 0.9;
            }}

            .container {{
                display: flex;
                height: calc(100vh - 100px);
            }}

            .sidebar {{
                width: 350px;
                background: #f8f9fa;
                overflow-y: auto;
                border-right: 1px solid #dee2e6;
                box-shadow: 2px 0 5px rgba(0,0,0,0.05);
            }}

            .sidebar-header {{
                padding: 20px;
                background: white;
                border-bottom: 2px solid #e9ecef;
            }}

            .sidebar-header h2 {{
                margin: 0 0 10px 0;
                font-size: 18px;
                color: #2c3e50;
            }}

            .view-all-btn {{
                width: 100%;
                padding: 10px;
                background: #667eea;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 14px;
                font-weight: 600;
                transition: background 0.3s;
            }}

            .view-all-btn:hover {{
                background: #5568d3;
            }}

            .newspaper-item {{
                padding: 15px 20px;
                border-bottom: 1px solid #e9ecef;
                cursor: pointer;
                transition: all 0.3s;
                background: white;
                margin: 5px 10px;
                border-radius: 5px;
            }}

            .newspaper-item:hover {{
                background: #e3f2fd;
                transform: translateX(5px);
            }}

            .newspaper-name {{
                font-weight: 600;
                color: #2c3e50;
                font-size: 15px;
                margin-bottom: 5px;
            }}

            .newspaper-location {{
                font-size: 13px;
                color: #7f8c8d;
            }}

            .map-container {{
                flex: 1;
                position: relative;
            }}

            #map {{
                width: 100%;
                height: 100%;
            }}

            .legend {{
                position: absolute;
                bottom: 30px;
                right: 30px;
                background: white;
                padding: 15px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.2);
                z-index: 1000;
                font-size: 13px;
            }}

            .legend h4 {{
                margin: 0 0 10px 0;
                font-size: 14px;
                color: #2c3e50;
            }}

            .legend-item {{
                margin: 5px 0;
                display: flex;
                align-items: center;
            }}

            .legend-icon {{
                width: 20px;
                height: 20px;
                margin-right: 10px;
                background: #a94442;
                border-radius: 50%;
            }}

            @media (max-width: 768px) {{
                .sidebar {{
                    width: 100%;
                    height: 300px;
                    border-right: none;
                    border-bottom: 1px solid #dee2e6;
                }}

                .container {{
                    flex-direction: column;
                }}

                .header h1 {{
                    font-size: 20px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>African American Newspapers in the United States</h1>
            <p>Exploring the legacy and locations of 20 historic and active African American periodicals</p>
        </div>

        <div class="container">
            <div class="sidebar">
                <div class="sidebar-header">
                    <h2>Select a Newspaper</h2>
                    <button class="view-all-btn" onclick="viewAll()">
                        <i class="fa fa-globe"></i> View All Locations
                    </button>
                </div>
                <div class="newspaper-list">
                    {newspapers_list}
                </div>
            </div>

            <div class="map-container">
                <div id="map"></div>
                <div class="legend">
                    <h4><i class="fa fa-info-circle"></i> Legend</h4>
                    <div class="legend-item">
                        <div class="legend-icon"></div>
                        <span>African American Newspaper</span>
                    </div>
                </div>
            </div>
        </div>

        <script>
            // This will be populated by Folium
            var map = null;

            function flyToLocation(lat, lng, name) {{
                if (map) {{
                    map.flyTo([lat, lng], 12, {{
                        duration: 1.5
                    }});
                }}
            }}

            function viewAll() {{
                if (map) {{
                    map.flyTo([39.8283, -98.5795], 4, {{
                        duration: 1.5
                    }});
                }}
            }}

            // Wait for map to be initialized by Folium
            setTimeout(function() {{
                // Get the Folium map object
                var mapElements = document.querySelectorAll('.folium-map');
                if (mapElements.length > 0) {{
                    var mapId = mapElements[0].id;
                    map = window[mapId];
                }}
            }}, 1000);
        </script>
    </body>
    </html>
    """

    return custom_html

def generate_html_file(periodicals, output_file='index.html'):
    """Generate the final HTML file."""

    # Create the base map
    m = create_newspaper_map(periodicals)

    # Save to HTML
    m.save(output_file)

    # Read the generated HTML
    with open(output_file, 'r') as f:
        folium_html = f.read()

    # Extract just the map initialization JavaScript and div
    # We'll inject this into our custom template
    import re

    # Find the map div and script
    map_div_match = re.search(r'<div class="folium-map"[^>]*>.*?</div>', folium_html, re.DOTALL)
    map_scripts_match = re.search(r'<script>.*?</script>.*?<script>.*?</script>', folium_html, re.DOTALL)

    if map_div_match and map_scripts_match:
        map_div = map_div_match.group(0)
        map_scripts = map_scripts_match.group(0)

        # Create custom HTML with embedded map
        custom_html = inject_dashboard_html(m, periodicals)

        # Replace the map container div with Folium's map
        custom_html = custom_html.replace('<div id="map"></div>', map_div)

        # Add Folium's scripts before closing body tag
        custom_html = custom_html.replace('</body>', f'{map_scripts}</body>')

        # Add Leaflet CSS and JS
        leaflet_css = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.css"/>'
        leaflet_js = '<script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.js"></script>'

        custom_html = custom_html.replace('</head>', f'{leaflet_css}</head>')
        custom_html = custom_html.replace('</body>', f'{leaflet_js}</body>')

        # Write final HTML
        with open(output_file, 'w') as f:
            f.write(custom_html)
    else:
        # Fallback: use Folium's HTML directly with some modifications
        print("Using fallback method - generating simple map")
        m.save(output_file)

    print(f"Map successfully generated: {output_file}")
    print(f"Total newspapers mapped: {len(periodicals)}")

def main():
    """Main execution function."""
    print("Loading periodicals data...")
    periodicals = load_periodicals_data()

    print(f"Found {len(periodicals)} African American newspapers")

    print("Generating interactive map...")
    generate_html_file(periodicals)

    print("\nDone! Open 'index.html' in your web browser to view the map.")
    print("This file is ready to be deployed on GitHub Pages.")

if __name__ == "__main__":
    main()
