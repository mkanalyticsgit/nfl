# TASKS.md — Backlog & Active Work

Edit this file anytime to add, reprioritise, or clarify requirements.
At the start of a new session tell the AI: "Read CLAUDE.md and TASKS.md, then work through the tasks."

---

## In Progress
<!-- Move items here when actively being worked on -->


---

## Up Next (prioritised)

<!-- All MVP tasks complete! Pick from Ideas/Future below. -->

---

## Ideas / Future
<!-- Not committed, just capturing -->

- Ad placement (banner slots in layout — define placement before implementing)
- AI features (Claude-powered player summaries / matchup analysis — deferred)
- Player search history / favourites (localStorage)
- Mobile nav improvements
- Dark/light mode toggle

---

## Completed
<!-- Move items here when done so there's a record -->

- [x] `backend/data/fetch.py` — nflverse data pipeline
- [x] `backend/data/cache.py` — DuckDB query helpers + NaN sanitisation
- [x] `backend/main.py` — FastAPI app with CORS
- [x] `backend/routes/players.py` — search, info, seasonal, weekly endpoints
- [x] `backend/routes/matchups.py` — upcoming games, defense stats, player matchup
- [x] Frontend scaffold — Vite + React + Tailwind + Recharts
- [x] `frontend/src/pages/SearchPage.jsx` — debounced player search
- [x] `frontend/src/pages/PlayerPage.jsx` — bio card (with headshot + correct height format), charts, stat tables
- [x] `frontend/src/pages/MatchupPage.jsx` — opponent defense radar chart
- [x] All backend endpoints tested and verified working
- [x] Frontend polish — headshot display, height ft/in format, Tailwind class fixes
- [x] `frontend/src/pages/ComparisonPage.jsx` — side-by-side player comparison with shared line chart and per-season stat table
- [x] PlayerPage O/U lines — per-stat over/under reference lines (red dashed) on weekly & seasonal charts; opponent abbreviation shown on weekly X-axis
- [x] PlayerPage O/U hit rate — whole-number-only inputs; hit rate summary cards (% over, X/Y games) with colour coding (green/yellow/red)
- [x] Deploy backend to Render.com — `render.yaml` with build/start commands, env vars, auto-deploy
- [x] Deploy frontend to Vercel — `vercel.json` with SPA rewrites; `VITE_API_BASE` for prod API URL
- [x] Weekly data refresh — `data/refresh.py` incrementally updates a single season (rosters, schedules, weekly, seasonal)
- [x] Chart legend moved to top — prevents overlap with rotated X-axis labels on all charts
- [x] Seasonal chart X-axis reversed — earliest season on left, latest on right
- [x] 2025 season data — rosters & schedules now include 2025; stats awaiting nflverse publish
- [x] Removed ComparisonPage — route, nav link, and file deleted
- [x] MatchupPage player season avg tile — shows selected player's per-game averages alongside defence averages
- [x] MatchupPage row exclusion — checkboxes on each game row; defence avg, hit rates, chart all recalculate dynamically
- [x] O/U hit rate labels — reworded to "stat > threshold vs OPP" with "X / Y games over"
- [x] Player search filter — only returns QB, RB, FB, WR, TE positions
- [x] PlayerPage game exclusion — weekly stat table has per-row checkboxes; chart & hit rates recalculate from included games only
