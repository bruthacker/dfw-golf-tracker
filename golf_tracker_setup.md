# Golf Course Tracker Setup

## Import the CSV
1. Open Google Sheets
2. File > Import > Upload `golf_tracker_template.csv`
3. Rename the tab to "Courses"

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

### Stats (Played Courses Only)
| Cell | Label | Formula |
|------|-------|---------|
| A6 | **Avg Rating** | |
| B6 | (value) | `=ROUND(AVERAGEIF(Courses!B:B,"Played",Courses!L:L),1)` |
| A7 | **Highest Rated** | |
| B7 | (name) | `=INDEX(Courses!A:A,MATCH(MAX(Courses!L:L),Courses!L:L,0))` |
| A8 | **Avg Score (Me)** | |
| B8 | (value) | `=ROUND(AVERAGE(Courses!N:N),1)` |

---

## Dropdown Validations

### Status (Column B)
1. Select column B
2. Data > Data validation > Dropdown
3. Options: `To Play`, `Played`, `Skipped`

### Time of Day (Column J)
1. Select column J
2. Data > Data validation > Dropdown
3. Options: `Dawn Patrol`, `Morning`, `Midday`, `Afternoon`, `Twilight`

### Conditions When Played (Column K)
1. Select column K
2. Data > Data validation > Dropdown
3. Options:
   - `Perfect` - Ideal weather and course conditions
   - `Great` - Minor issues but excellent overall
   - `Good` - Playable, some wind/heat/wet spots
   - `Fair` - Weather or conditions impacted play
   - `Poor` - Tough conditions, hard to judge course fairly
   - `Cart Path Only` - Recent rain, restricted to paths

### My Rating (Column L)
1. Select column L
2. Data > Data validation > Dropdown
3. Options: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`

---

## Auto-Generate Google Maps Links
If you add a course manually and just enter the name + city, use this formula:
```
=HYPERLINK("https://www.google.com/maps/search/?api=1&query="&SUBSTITUTE(A2&" "&C2," ","+"), "Map")
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
1. Select column L
2. Format > Conditional formatting > Color scale
3. Min (1) = Red, Mid (5) = Yellow, Max (10) = Green

### Conditions Colors
1. Select column K
2. Rules:
   - Text contains "Perfect" → Dark green text
   - Text contains "Poor" or "Cart Path" → Orange text

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
