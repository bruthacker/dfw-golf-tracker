# Golf Course Tracker Setup

## Import the CSV
1. Open Google Sheets
2. File > Import > Upload `golf_tracker_template.csv`
3. Rename the tab to "Courses"

---

## Price Tiers (Color-Coded)

| Tier | Symbol | Price Range | Suggested Color |
|------|--------|-------------|-----------------|
| **Budget** | $ | Under $60 | Green (#d9ead3) |
| **Value** | $$ | $60-80 | Blue (#cfe2f3) |
| **Premium** | $$$ | $80-125 | Orange (#fce5cd) |
| **Luxury** | $$$$ | $125+ | Purple (#d9d2e9) |

### Apply Price Tier Colors
1. Select the Price Tier column (Column I)
2. Format > Conditional formatting
3. Add rules:
   - Text is exactly `$` → Green background (#d9ead3)
   - Text is exactly `$$` → Blue background (#cfe2f3)
   - Text is exactly `$$$` → Orange background (#fce5cd)
   - Text is exactly `$$$$` → Purple background (#d9d2e9)

---

## Priority System

Use to mark which courses you want to play next.

| Priority | Meaning |
|----------|---------|
| **1 - Next Up** | Play this one ASAP |
| **2 - Soon** | On the short list |
| **3 - Eventually** | Want to play, no rush |
| *(blank)* | Not prioritized yet |

### Priority Dropdown (Column C)
1. Select column C
2. Data > Data validation > Dropdown
3. Options: `1 - Next Up`, `2 - Soon`, `3 - Eventually`

### Priority Colors (Optional)
1. Select column C
2. Format > Conditional formatting
3. Rules:
   - Text contains "Next Up" → Red background (#f4cccc)
   - Text contains "Soon" → Yellow background (#fff2cc)
   - Text contains "Eventually" → Light gray (#efefef)

---

## Rating System (1-10)

| Rating | Label | Description |
|--------|-------|-------------|
| **10** | Elite | Bucket list course. World-class in every way. Would travel far to replay. |
| **9** | Exceptional | Outstanding course. Memorable holes, excellent conditions, great experience. |
| **8** | Excellent | High quality course. Well above average in design, conditions, or both. |
| **7** | Very Good | Solid course worth revisiting. Good layout, good conditions. |
| **6** | Good | Above average. Enjoyable round, some memorable moments. |
| **5** | Average | Decent course. Nothing special but nothing wrong either. |
| **4** | Below Average | Some issues - poor conditions, boring layout, or bad pace of play. |
| **3** | Disappointing | Multiple problems. Wouldn't recommend unless convenient/cheap. |
| **2** | Poor | Significant issues. Only play if desperate for a round. |
| **1** | Avoid | Do not return. Major problems with course, service, or value. |

---

## Create Dashboard Tab
1. Add a new tab called "Dashboard"
2. Use these formulas (assuming your data starts in row 2 of "Courses" tab):

### Course Counts
| Cell | Label | Formula |
|------|-------|---------|
| A1 | **Courses To Play** | |
| B1 | (count) | `=COUNTIF(Courses!B:B,"To Play")` |
| A2 | **Courses Played** | |
| B2 | (count) | `=COUNTIF(Courses!B:B,"Played")` |
| A3 | **Total Courses** | |
| B3 | (count) | `=COUNTA(Courses!A:A)-1` |
| A4 | **Completion %** | |
| B4 | (value) | `=ROUND(B2/B3*100,1)&"%"` |

### Priority Counts
| Cell | Label | Formula |
|------|-------|---------|
| A6 | **Next Up** | |
| B6 | (count) | `=COUNTIF(Courses!C:C,"1 - Next Up")` |
| A7 | **Soon** | |
| B7 | (count) | `=COUNTIF(Courses!C:C,"2 - Soon")` |

### Stats (Played Courses Only)
| Cell | Label | Formula |
|------|-------|---------|
| A9 | **Avg Rating** | |
| B9 | (value) | `=ROUND(AVERAGEIF(Courses!B:B,"Played",Courses!N:N),1)` |
| A10 | **Highest Rated** | |
| B10 | (name) | `=INDEX(Courses!A:A,MATCH(MAX(Courses!N:N),Courses!N:N,0))` |
| A11 | **Avg Score (Me)** | |
| B11 | (value) | `=ROUND(AVERAGE(Courses!P:P),1)` |

### Price Tier Breakdown
| Cell | Label | Formula |
|------|-------|---------|
| A13 | **Budget ($)** | |
| B13 | (count) | `=COUNTIF(Courses!I:I,"$")` |
| A14 | **Value ($$)** | |
| B14 | (count) | `=COUNTIF(Courses!I:I,"$$")` |
| A15 | **Premium ($$$)** | |
| B15 | (count) | `=COUNTIF(Courses!I:I,"$$$")` |
| A16 | **Luxury ($$$$)** | |
| B16 | (count) | `=COUNTIF(Courses!I:I,"$$$$")` |

---

## Dropdown Validations

### Status (Column B)
1. Select column B
2. Data > Data validation > Dropdown
3. Options: `To Play`, `Played`, `Skipped`

### Priority (Column C)
1. Select column C
2. Data > Data validation > Dropdown
3. Options: `1 - Next Up`, `2 - Soon`, `3 - Eventually`

### Price Tier (Column I)
1. Select column I
2. Data > Data validation > Dropdown
3. Options: `$`, `$$`, `$$$`, `$$$$`

### Time of Day (Column L)
1. Select column L
2. Data > Data validation > Dropdown
3. Options: `Dawn Patrol`, `Morning`, `Midday`, `Afternoon`, `Twilight`

### Conditions When Played (Column M)
1. Select column M
2. Data > Data validation > Dropdown
3. Options:
   - `Perfect` - Ideal weather and course conditions
   - `Great` - Minor issues but excellent overall
   - `Good` - Playable, some wind/heat/wet spots
   - `Fair` - Weather or conditions impacted play
   - `Poor` - Tough conditions, hard to judge course fairly
   - `Cart Path Only` - Recent rain, restricted to paths

### My Rating (Column N)
1. Select column N
2. Data > Data validation > Dropdown
3. Options: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`

---

## Auto-Generate Google Maps Links
If you add a course manually and just enter the name + city, use this formula:
```
=HYPERLINK("https://www.google.com/maps/search/?api=1&query="&SUBSTITUTE(A2&" "&D2," ","+"), "Map")
```

---

## Conditional Formatting Suggestions

### Status Colors
1. Select column B (or full rows)
2. Format > Conditional formatting
3. Rules:
   - Text is "To Play" → Light yellow background
   - Text is "Played" → Light green background
   - Text is "Skipped" → Light gray background

### Rating Colors
1. Select column N
2. Format > Conditional formatting > Color scale
3. Min (1) = Red, Mid (5) = Yellow, Max (10) = Green

### Conditions Colors
1. Select column M
2. Rules:
   - Text contains "Perfect" → Dark green text
   - Text contains "Poor" or "Cart Path" → Orange text

---

## Column Reference

| Column | Field |
|--------|-------|
| A | Course Name |
| B | Status |
| C | Priority |
| D | City |
| E | Address |
| F | Google Maps Link |
| G | Website |
| H | Booking Link |
| I | Price Tier |
| J | Price Range |
| K | Date Played |
| L | Time of Day |
| M | Conditions When Played |
| N | My Rating (1-10) |
| O | Player 1 |
| P | Score 1 |
| Q | Player 2 |
| R | Score 2 |
| S | Player 3 |
| T | Score 3 |
| U | Player 4 |
| V | Score 4 |
| W | Notes |

---

## Included Courses (38 total)

### AvidGolfer 2025 - Best Overall
1. Texas Star Golf Course (Euless) - Best Overall West
2. Fields Ranch West (Frisco) - Best Overall East

### AvidGolfer 2025 - Platinum ($125+)
3. Bridlewood Golf Club (Flower Mound)
4. Fields Ranch East (Frisco)
5. Heritage Ranch Golf & CC (McKinney)
6. Old American Golf Club (The Colony)
7. Sky Creek Ranch Golf Club (Keller)
8. Texas Rangers Golf Club (Arlington)
9. The Tribute Golf Links (The Colony)
10. Tour 18 Dallas (Flower Mound)
11. Wildhorse at Robson Ranch (Denton)

### AvidGolfer 2025 - Elite ($80-$125)
12. Bear Creek Golf Club - West (Dallas)
13. Buffalo Creek Golf Club (Rockwall)
14. Frisco Lakes Golf Club (Frisco)
15. Indian Creek Golf Club - Creek (Carrollton)
16. The Golf Club at Fossil Creek (Fort Worth)
17. The Golf Club at Twin Creeks (Allen)
18. The Trails of Frisco Golf Club (Frisco)
19. Tierra Verde Golf Club (Arlington)
20. Waterchase Golf Club (Fort Worth)

### AvidGolfer 2025 - Top Luxury ($60-$80)
21. Brazos Club / Sugar Tree (Lipan)
22. Firewheel Golf Park - Bridges (Garland)
23. Grapevine Golf Course (Grapevine)
24. Hawks Creek Golf Club (Westworth Village)
25. Meadowbrook Golf Course (Fort Worth)
26. Sherrill Park Golf Course No. 1 (Richardson)
27. Southern Oaks Golf & Tennis (Burleson)
28. Tangle Ridge Golf Course (Grand Prairie)
29. The Bridges Golf Club (Gunter)
30. The Courses at Watters Creek (Plano)

### AvidGolfer 2025 - Best Outlying Courses
31. Tempest Golf Club (Gladewater)
32. Pine Dunes Resort & Golf Club (Frankston)
33. The Cliffs Resort (Graford)
34. The Links at Land's End (Yantis)
35. White Bluff Resort (Whitney)
36. Turtle Hill Golf Course (Muenster)

### Additional Courses
37. Squaw Valley - Apache Links (Glen Rose) - #1 Muni in TX
38. Squaw Valley - Comanche Lakes (Glen Rose) - #4 Muni in TX
