## NBA Bench Data – Dataset Schema

### Files
- `data/{year}/season.jsonl`: Regular season player aggregates (per game), one JSON object per line.
- `data/{year}/postseason.jsonl`: Postseason player aggregates (per game), one JSON object per line.

Both files in a given year share the same schema. Data is provided for both the 2023-24 and 2024-25 seasons.

### General conventions
- Records are JSON Lines (JSONL): exactly one valid JSON object per line.
- All rate/count stats are per game unless stated otherwise.
- Percentages are decimals in the range [0, 1] (e.g., 0.529 means 52.9%).
- Minutes are decimal minutes per game (e.g., 35.4).
- Team abbreviations use standard NBA short codes (e.g., `LAL`, `BOS`).
- Player team (`team`) reflects the team at the end of the season/year.

### Record schema (common to season and postseason)
- **rank**: integer – Rank within the year/file.
- **player**: string – Player name.
- **position**: string – Primary position (`PG`, `SG`, `SF`, `PF`, `C`).
- **team**: string – NBA team abbreviation (end-of-year team).
- **gp**: integer – Games played.
- **mpg**: number – Minutes per game.
- **fg_pct**: number – Field goal percentage (0–1).
- **ft_pct**: number – Free throw percentage (0–1).
- **three_pm**: number – 3-point field goals made per game.
- **rpg**: number – Rebounds per game.
- **apg**: number – Assists per game.
- **stpg**: number – Steals per game.
- **blkpg**: number – Blocks per game.
- **topg**: number – Turnovers per game.
- **pts**: number – Points per game.
- **rating**: number – Composite player rating metric.
- **id**: integer – Player identifier.

### Notes
- Season and postseason files have identical fields; values are computed over the respective games in that context.
