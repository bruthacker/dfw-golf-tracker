#!/usr/bin/env python3
"""
Generate a KML file from the golf tracker CSV for Google My Maps import.
Markers are color-coded by Price Tier and Status.
"""

import csv
import html
from pathlib import Path

# KML color codes (AABBGGRR format - alpha, blue, green, red)
COLORS = {
    # Price tiers
    "$": "ff00aa00",      # Green - Budget
    "$$": "ffff8800",     # Blue - Value
    "$$$": "ff0088ff",    # Orange - Premium
    "$$$$": "ffff00ff",   # Purple - Luxury
    # Status
    "Played": "ff00ff00",  # Bright green
    "To Play": "ff0000ff", # Red
}

# Pin styles
STYLE_PLAYED = "grn-circle"
STYLE_TO_PLAY = "red-circle"

def escape_xml(text):
    """Escape special XML characters."""
    if text is None:
        return ""
    return html.escape(str(text))

def generate_kml(csv_path: str, output_path: str, spreadsheet_url: str = None):
    """Generate a KML file from the CSV."""

    courses = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            courses.append(row)

    # Build KML
    kml_parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<kml xmlns="http://www.opengis.net/kml/2.2">',
        '<Document>',
        '<name>DFW Golf Course Tracker</name>',
    ]

    # Add description with link to spreadsheet
    desc = "Personal golf course tracker - DFW and beyond"
    if spreadsheet_url:
        desc += f'\n\nView/Edit Spreadsheet: {spreadsheet_url}'
    kml_parts.append(f'<description>{escape_xml(desc)}</description>')

    # Define styles for each price tier and status combination
    styles = [
        # Played courses - circle icons
        ("played-budget", "http://maps.google.com/mapfiles/kml/paddle/grn-circle.png", "ff00aa00"),
        ("played-value", "http://maps.google.com/mapfiles/kml/paddle/blu-circle.png", "ffff8800"),
        ("played-premium", "http://maps.google.com/mapfiles/kml/paddle/orange-circle.png", "ff0088ff"),
        ("played-luxury", "http://maps.google.com/mapfiles/kml/paddle/purple-circle.png", "ffff00ff"),
        # To Play courses - blank icons
        ("toplay-budget", "http://maps.google.com/mapfiles/kml/paddle/grn-blank.png", "ff00aa00"),
        ("toplay-value", "http://maps.google.com/mapfiles/kml/paddle/blu-blank.png", "ffff8800"),
        ("toplay-premium", "http://maps.google.com/mapfiles/kml/paddle/orange-blank.png", "ff0088ff"),
        ("toplay-luxury", "http://maps.google.com/mapfiles/kml/paddle/purple-blank.png", "ffff00ff"),
    ]

    for style_id, icon_url, color in styles:
        kml_parts.append(f'''<Style id="{style_id}">
    <IconStyle>
        <Icon><href>{icon_url}</href></Icon>
        <scale>1.2</scale>
    </IconStyle>
</Style>''')

    # Create folders for organization
    played_courses = [c for c in courses if c.get('Status') == 'Played']
    toplay_courses = [c for c in courses if c.get('Status') == 'To Play']

    def get_style_id(course):
        status = course.get('Status', 'To Play')
        tier = course.get('Price Tier', '$$')
        prefix = "played" if status == "Played" else "toplay"
        tier_map = {"$": "budget", "$$": "value", "$$$": "premium", "$$$$": "luxury"}
        tier_name = tier_map.get(tier, "value")
        return f"{prefix}-{tier_name}"

    def create_placemark(course):
        name = escape_xml(course.get('Course Name', 'Unknown'))
        city = escape_xml(course.get('City', ''))
        address = escape_xml(course.get('Address', ''))
        website = course.get('Website', '')
        booking = course.get('Booking Link', '')
        price_tier = escape_xml(course.get('Price Tier', ''))
        price_range = escape_xml(course.get('Price Range', ''))
        notes = escape_xml(course.get('Notes', ''))
        status = course.get('Status', 'To Play')
        rating = course.get('My Rating (1-10)', '')

        # Build description HTML
        desc_parts = []
        if price_tier and price_range:
            desc_parts.append(f"<b>Price:</b> {price_tier} ({price_range})")
        if status == "Played" and rating:
            desc_parts.append(f"<b>My Rating:</b> {rating}/10")
        if notes:
            desc_parts.append(f"<b>Notes:</b> {notes}")
        if website:
            desc_parts.append(f'<a href="{escape_xml(website)}">Website</a>')
        if booking:
            desc_parts.append(f'<a href="{escape_xml(booking)}">Book Tee Time</a>')

        description = "<br/>".join(desc_parts)
        style_id = get_style_id(course)

        # Use address for positioning (Google Earth/Maps will geocode it)
        full_address = f"{address}" if address else city

        return f'''<Placemark>
    <name>{name}</name>
    <description><![CDATA[{description}]]></description>
    <styleUrl>#{style_id}</styleUrl>
    <address>{escape_xml(full_address)}</address>
</Placemark>'''

    # Played folder
    kml_parts.append('<Folder>')
    kml_parts.append(f'<name>Played ({len(played_courses)})</name>')
    for course in played_courses:
        kml_parts.append(create_placemark(course))
    kml_parts.append('</Folder>')

    # To Play folder
    kml_parts.append('<Folder>')
    kml_parts.append(f'<name>To Play ({len(toplay_courses)})</name>')
    for course in toplay_courses:
        kml_parts.append(create_placemark(course))
    kml_parts.append('</Folder>')

    kml_parts.append('</Document>')
    kml_parts.append('</kml>')

    # Write KML file
    kml_content = '\n'.join(kml_parts)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(kml_content)

    print(f"Generated {output_path}")
    print(f"  - {len(played_courses)} played courses")
    print(f"  - {len(toplay_courses)} courses to play")
    print(f"  - {len(courses)} total")
    print()
    print("To import into Google My Maps:")
    print("1. Go to https://www.google.com/maps/d/")
    print("2. Create a new map (or open existing)")
    print("3. Click 'Import' in the left panel")
    print("4. Upload this KML file")
    print()
    print("Color Legend:")
    print("  Green  = Budget ($, under $60)")
    print("  Blue   = Value ($$, $60-80)")
    print("  Orange = Premium ($$$, $80-125)")
    print("  Purple = Luxury ($$$$, $125+)")
    print("  Circle = Played")
    print("  Blank  = To Play")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate KML map from golf tracker CSV")
    parser.add_argument("--csv", default="golf_tracker_template.csv", help="Input CSV file")
    parser.add_argument("--output", "-o", default="dfw_golf_courses.kml", help="Output KML file")
    parser.add_argument("--spreadsheet-url", help="URL to your Google Sheets spreadsheet")

    args = parser.parse_args()

    generate_kml(args.csv, args.output, args.spreadsheet_url)
