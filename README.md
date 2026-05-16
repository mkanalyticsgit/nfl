# NFL Player Analytics Tool 🏈

A free, web-based NFL player analytics tool powered by Python, React, and Claude AI. Compare player stats, analyze matchups, and get AI-generated insights — no subscription required.

---

## What It Does

- **Player Stats** — Search any NFL player and view historical stats (passing yards, touchdowns, rushing yards, receiving yards, and more)
- **Matchup Analysis** — Compare a player's performance history against their upcoming opponent's defensive rankings
- **AI Insights** — Claude-powered summaries and natural language queries ("How has Patrick Mahomes performed against top defenses?")
- **Player Comparison** — Side-by-side stat comparison between two players

---

## Tech Stack

| Layer | Technology |
|---|---|
| Data | `nfl_data_py` (Python port of nflverse) |
| Backend | Python + FastAPI |
| Database | DuckDB (file-based, no server needed) |
| Frontend | React + Tailwind CSS |
| AI | Anthropic Claude API |
| Hosting | Render.com (backend) + Vercel (frontend) |
| Dev Environment | GitHub Codespaces |

---

## Project Structure

```
nfl-analytics/
├── backend/
│   ├── main.py              # FastAPI app entry point
│   ├── data/
│   │   ├── fetch.py         # nfl_data_py data pipeline
│   │   ├── cache.py         # DuckDB caching layer
│   │   └── nfl.duckdb       # Local data store (git-ignored)
│   ├── routes/
│   │   ├── players.py       # Player search & stats endpoints
│   │   ├── matchups.py      # Opponent analysis endpoints
│   │   └── ask.py           # Claude AI natural language endpoint
│   ├── claude/
│   │   ├── prompts.py       # System prompts & prompt templates
│   │   └── agent.py         # Claude tool-use agent logic
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # App pages
│   │   └── App.jsx
│   ├── package.json
│   └── index.html
├── data/
│   └── refresh.py           # Weekly data refresh script (run manually)
├── .devcontainer/
│   └── devcontainer.json    # GitHub Codespaces config
├── .env.example             # Environment variable template
├── .gitignore
└── README.md
```

---

## Getting Started

### Prerequisites

- GitHub account (free)
- Anthropic API key ([get one here](https://console.anthropic.com))

### Run in GitHub Codespaces (Recommended)

1. Fork or clone this repo on GitHub
2. Click the green **Code** button → **Codespaces** tab → **Create codespace on main**
3. Wait ~60 seconds for the environment to boot
4. In the terminal, run the setup script:

```bash
bash scripts/setup.sh
```

5. Copy `.env.example` to `.env` and add your Anthropic API key:

```bash
cp .env.example .env
# Edit .env and add: ANTHROPIC_API_KEY=your_key_here
```

6. Load NFL data (first time only, takes ~2 minutes):

```bash
cd backend && python data/fetch.py
```

7. Start the backend:

```bash
cd backend && uvicorn main:app --reload
```

8. In a new terminal, start the frontend:

```bash
cd frontend && npm install && npm run dev
```

### Run Locally (VS Code)

Same steps as above, just run directly in your VS Code terminal instead of Codespaces.

---

## Environment Variables

Copy `.env.example` to `.env` and fill in:

```
ANTHROPIC_API_KEY=your_anthropic_api_key
```

Never commit your `.env` file. It is already in `.gitignore`.

---

## Data

NFL stats are sourced from [`nfl_data_py`](https://github.com/nflverse/nfl_data_py), the Python port of the R `nflverse` package. Data covers:

- Player seasonal and weekly stats (2000–present)
- Roster and player metadata
- Schedule and opponent data
- Team defensive rankings

Run `python data/refresh.py` to pull the latest data. During the season, refresh weekly.

---

## Claude AI Integration

This project uses the Claude API for three features:

- **Player Summaries** — Structured stats sent to Claude, narrative insight returned
- **Matchup Analysis** — Player history + opponent defensive data → prediction and context
- **Natural Language Queries** — Claude uses tool-calling to decide what data to fetch and how to answer free-form questions

System prompts and agent logic live in `backend/claude/`.

---

## Cost

This project is designed to run at near-zero cost:

- All infrastructure uses free tiers (Render, Vercel, GitHub Codespaces)
- Claude API calls are cached — identical queries return stored results
- At low traffic, API costs are estimated at under $5/month

---

## Roadmap

- [x] Project structure and README
- [ ] Data pipeline (`nfl_data_py` + DuckDB)
- [ ] FastAPI backend with player and matchup endpoints
- [ ] Claude AI integration (summaries, matchup analysis, NL queries)
- [ ] React frontend with player search and stat charts
- [ ] Deployment to Render + Vercel
- [ ] Google AdSense integration

---

## Contributing

This is a personal prototype project. Contributions, suggestions, and feedback welcome via GitHub Issues.

---

## License

MIT License — free to use, modify, and distribute.
