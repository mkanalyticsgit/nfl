import nfl_data_py as nfl
import duckdb
import pandas as pd
from pathlib import Path

# Path to local DuckDB file
DB_PATH = Path(__file__).parent / "nfl.duckdb"

def get_connection():
    return duckdb.connect(str(DB_PATH))

def fetch_and_store_seasonal_stats(seasons: list[int] = None):
    """Fetch seasonal player stats and store in DuckDB."""
    if seasons is None:
        seasons = list(range(2019, 2025))

    print(f"Fetching seasonal stats for {seasons}...")
    df = nfl.import_seasonal_data(seasons)
    df.columns = df.columns.str.lower()

    con = get_connection()
    con.execute("DROP TABLE IF EXISTS seasonal_stats")
    con.execute("CREATE TABLE seasonal_stats AS SELECT * FROM df")
    count = con.execute("SELECT COUNT(*) FROM seasonal_stats").fetchone()[0]
    con.close()
    print(f"Stored {count} rows in seasonal_stats")

def fetch_and_store_weekly_stats(seasons: list[int] = None):
    """Fetch weekly player stats and store in DuckDB."""
    if seasons is None:
        seasons = list(range(2019, 2025))

    print(f"Fetching weekly stats for {seasons}...")
    df = nfl.import_weekly_data(seasons)
    df.columns = df.columns.str.lower()

    con = get_connection()
    con.execute("DROP TABLE IF EXISTS weekly_stats")
    con.execute("CREATE TABLE weekly_stats AS SELECT * FROM df")
    count = con.execute("SELECT COUNT(*) FROM weekly_stats").fetchone()[0]
    con.close()
    print(f"Stored {count} rows in weekly_stats")

def fetch_and_store_rosters(seasons: list[int] = None):
    """Fetch roster data and store in DuckDB."""
    if seasons is None:
        seasons = list(range(2019, 2025))

    print(f"Fetching rosters for {seasons}...")
    df = nfl.import_rosters(seasons)
    df.columns = df.columns.str.lower()

    con = get_connection()
    con.execute("DROP TABLE IF EXISTS rosters")
    con.execute("CREATE TABLE rosters AS SELECT * FROM df")
    count = con.execute("SELECT COUNT(*) FROM rosters").fetchone()[0]
    con.close()
    print(f"Stored {count} rows in rosters")

def fetch_and_store_schedules(seasons: list[int] = None):
    """Fetch schedule data and store in DuckDB."""
    if seasons is None:
        seasons = list(range(2019, 2025))

    print(f"Fetching schedules for {seasons}...")
    df = nfl.import_schedules(seasons)
    df.columns = df.columns.str.lower()

    con = get_connection()
    con.execute("DROP TABLE IF EXISTS schedules")
    con.execute("CREATE TABLE schedules AS SELECT * FROM df")
    count = con.execute("SELECT COUNT(*) FROM schedules").fetchone()[0]
    con.close()
    print(f"Stored {count} rows in schedules")

def show_tables():
    """Print a summary of what's in the database."""
    con = get_connection()
    tables = con.execute("SHOW TABLES").fetchall()
    print("\n--- Database Summary ---")
    for (table,) in tables:
        count = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        cols = con.execute(f"DESCRIBE {table}").fetchall()
        print(f"{table}: {count} rows, {len(cols)} columns")
    con.close()

if __name__ == "__main__":
    print("Starting NFL data pipeline...")
    fetch_and_store_rosters()
    fetch_and_store_schedules()
    fetch_and_store_seasonal_stats()
    fetch_and_store_weekly_stats()
    show_tables()
    print("\nDone! Data stored in backend/data/nfl.duckdb")