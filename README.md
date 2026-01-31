# DFW Golf Course Tracker

A personal tracker for public golf courses in the Dallas-Fort Worth metroplex and surrounding areas.

## Files

- **`golf_tracker_template.csv`** - The main spreadsheet with 38 courses, ready to import into Google Sheets
- **`golf_tracker_setup.md`** - Setup instructions, rating system, formulas, and course list
- **`CLAUDE.md`** - Instructions for Claude Code to update this project

## Quick Start

1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new spreadsheet
3. File > Import > Upload `golf_tracker_template.csv`
4. Follow the setup instructions in `golf_tracker_setup.md`

## What's Included

### 38 Public Golf Courses

Sourced from **AvidGolfer Magazine's 2025 Best of Public Golf** rankings:

| Tier | Price Range | Count |
|------|-------------|-------|
| Best Overall | Varies | 2 |
| Platinum | $125+ | 9 |
| Elite | $80-125 | 9 |
| Top Luxury | $60-80 | 10 |
| Best Outlying | Varies | 6 |
| Additional | Varies | 2 |

### Data for Each Course

- Course name and city
- Full address
- Google Maps link (clickable)
- Website
- Tee time booking link
- Price range
- Space for: date played, time of day, conditions, personal rating
- Scores for up to 4 players
- Notes

## Rating System

| Rating | Label | Description |
|--------|-------|-------------|
| 10 | Elite | Bucket list course. World-class. |
| 9 | Exceptional | Outstanding, memorable experience. |
| 8 | Excellent | High quality, well above average. |
| 7 | Very Good | Solid, worth revisiting. |
| 6 | Good | Above average, enjoyable. |
| 5 | Average | Nothing special, nothing wrong. |
| 4 | Below Average | Some issues present. |
| 3 | Disappointing | Multiple problems. |
| 2 | Poor | Significant issues. |
| 1 | Avoid | Do not return. |

## Google Maps Integration

### Import to Google My Maps

1. Go to [Google My Maps](https://www.google.com/maps/d/)
2. Click "Create a New Map"
3. Click "Import" in the left panel
4. Upload `dfw_golf_courses.kml`

### Or generate a fresh KML file:

```bash
python3 generate_map.py --spreadsheet-url "YOUR_GOOGLE_SHEETS_URL"
```

### Map Color Legend

| Color | Price Tier | Price Range |
|-------|------------|-------------|
| Green | $ (Budget) | Under $60 |
| Blue | $$ (Value) | $60-80 |
| Orange | $$$ (Premium) | $80-125 |
| Purple | $$$$ (Luxury) | $125+ |

- **Circle icons** = Played
- **Blank icons** = To Play

## Sources

- [AvidGolfer 2025 Best of Public Golf](https://myavidgolfer.com/cover-story-2025-best-of-public-golf/)
- Individual course websites for addresses and booking links
