# Claude Code Instructions

This file contains instructions for Claude Code to maintain and update this golf course tracker.

## Project Overview

This is a personal golf course tracker for DFW-area public courses. The main data file is `golf_tracker_template.csv` which is designed to be imported into Google Sheets.

## How to Update the Spreadsheet

### Adding a New Course Manually

1. Open `golf_tracker_template.csv`
2. Add a new row with the following columns (in order):
   ```
   Course Name, Status, Priority, City, Address, Google Maps Link, Website, Booking Link,
   Price Tier, Price Range, Date Played, Time of Day, Conditions When Played, My Rating (1-10),
   Player 1, Score 1, Player 2, Score 2, Player 3, Score 3, Player 4, Score 4, Notes
   ```

3. For **Price Tier**, use: `$` (under $60), `$$` ($60-80), `$$$` ($80-125), `$$$$` ($125+)

4. For the **Google Maps Link**, use this format:
   ```
   https://www.google.com/maps/search/?api=1&query=COURSE+NAME+CITY+TX
   ```
   Replace spaces with `+` signs.

4. Set **Status** to `To Play` for new courses.

5. Leave date, time, conditions, rating, and scores blank for courses not yet played.

### Example New Course Entry

```csv
Stevens Park Golf Course,To Play,,Dallas,"1005 N Montclair Ave, Dallas, TX 75208",https://www.google.com/maps/search/?api=1&query=Stevens+Park+Golf+Course+Dallas+TX,https://www.stevensparkgolf.com,https://www.stevensparkgolf.com/tee-times/,$$,$40-60,,,,,,,,,,,,Little Augusta - great downtown views
```

## How to Get More Course Information

When the user asks to add courses or update information:

1. **Search the web** for the course name + city + "TX" to find:
   - Official website
   - Address
   - Tee time booking page (often `/tee-times/` on the main site, or use GolfNow)

2. **For bulk updates** (e.g., new AvidGolfer rankings), fetch the source page and extract all courses.

3. **Verify addresses** by cross-referencing multiple sources (Yelp, Google, PGA.com).

4. **Price ranges** should reflect typical weekend rates:
   - Under $40: Budget
   - $40-60: Value
   - $60-80: Top Luxury
   - $80-125: Elite
   - $125+: Platinum/Premium

## Annual Updates

Each year around January, AvidGolfer Magazine publishes new rankings:
- URL pattern: `https://myavidgolfer.com/cover-story-YEAR-best-of-public-golf/`
- Fetch the page and extract all courses by tier
- Update the Notes column to reflect new rankings
- Add any new courses that appear on the list

## Data Sources to Check

- [AvidGolfer Magazine](https://myavidgolfer.com) - Annual rankings
- [GolfPass](https://www.golfpass.com) - Course details and reviews
- [Golf Digest](https://www.golfdigest.com/courses) - Ratings and course info
- [GolfNow](https://www.golfnow.com) - Tee times and pricing
- Individual course websites

## Validation Checklist

When adding or updating courses, verify:
- [ ] Course name is correct and matches the website
- [ ] Address includes street, city, state, and ZIP
- [ ] Google Maps link works when clicked
- [ ] Website URL is active
- [ ] Booking link goes to tee times (not homepage)
- [ ] Price range is current

## File Structure

```
golf-tracker/
├── README.md                    # Project overview
├── CLAUDE.md                    # This file - Claude instructions
├── golf_tracker_template.csv    # Main data file (import to Google Sheets)
├── golf_tracker_setup.md        # Setup instructions and formulas
├── generate_map.py              # Script to generate KML map file
└── dfw_golf_courses.kml         # Google My Maps import file
```

## Regenerating the Map

After updating the CSV, regenerate the KML file:

```bash
python3 generate_map.py
```

Or with a link back to the spreadsheet:

```bash
python3 generate_map.py --spreadsheet-url "https://docs.google.com/spreadsheets/d/YOUR_ID"
```

The KML file uses color-coded markers:
- **Green** = Budget ($)
- **Blue** = Value ($$)
- **Orange** = Premium ($$$)
- **Purple** = Luxury ($$$$)
- **Circle** = Played
- **Blank** = To Play

## CSV Column Reference

| Column | Description | Example |
|--------|-------------|---------|
| Course Name | Official name | Texas Star Golf Course |
| Status | To Play / Played / Skipped | To Play |
| Priority | 1 - Next Up / 2 - Soon / 3 - Eventually | 1 - Next Up |
| City | City name | Euless |
| Address | Full street address | 1400 Texas Star Pkwy, Euless, TX 76040 |
| Google Maps Link | Direct link to maps | https://www.google.com/maps/search/?api=1&query=... |
| Website | Course homepage | https://www.texasstargolf.com |
| Booking Link | Tee time reservation page | https://www.texasstargolf.com/tee-times/ |
| Price Tier | $ / $$ / $$$ / $$$$ | $$ |
| Price Range | Typical weekend rate | $50-80 |
| Date Played | YYYY-MM-DD format | 2025-03-15 |
| Time of Day | Dawn Patrol / Morning / Midday / Afternoon / Twilight | Morning |
| Conditions When Played | Perfect / Great / Good / Fair / Poor / Cart Path Only | Great |
| My Rating (1-10) | Personal rating | 8 |
| Player 1-4 | Names of playing partners | John |
| Score 1-4 | Their scores | 82 |
| Notes | Any additional info | AvidGolfer Best Overall West 2025 |

## Price Tier Definitions

| Tier | Symbol | Price Range | Color |
|------|--------|-------------|-------|
| Budget | $ | Under $60 | Green |
| Value | $$ | $60-80 | Blue |
| Premium | $$$ | $80-125 | Orange |
| Luxury | $$$$ | $125+ | Purple |
