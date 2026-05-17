# TASKS.md — Backlog & Active Work

Edit this file anytime to add, reprioritise, or clarify requirements.
At the start of a new session tell the AI: "Read CLAUDE.md and TASKS.md, then work through the tasks."

---

## In Progress
<!-- Move items here when actively being worked on -->


---

## Up Next (prioritised)

1. **Frontend — test & polish** — verify the 3 pages render correctly end-to-end; fix any layout/data issues found during testing
2. **Player comparison page** — side-by-side stat view for two players (search both, shared chart)
3. **Deploy backend to Render.com** — add `render.yaml`, set env vars, connect to hosted DuckDB or periodic fetch
4. **Deploy frontend to Vercel** — add `vercel.json`, set `VITE_API_BASE` to Render URL
5. **Weekly data refresh** — implement `data/refresh.py` to incrementally update the current season without full re-fetch

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
- [x] `frontend/src/pages/PlayerPage.jsx` — bio card, charts, stat tables
- [x] `frontend/src/pages/MatchupPage.jsx` — opponent defense radar chart
- [x] All backend endpoints tested and verified working
