import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/lol.db"
)

players = pd.read_sql(
    "SELECT * FROM players",
    conn
)

matches = pd.read_sql(
    "SELECT * FROM matches",
    conn
)

participants = pd.read_sql(
    "SELECT * FROM participants",
    conn
)

players.to_csv(
    "reports/players.csv",
    index=False
)

matches.to_csv(
    "reports/matches.csv",
    index=False
)

participants.to_csv(
    "reports/participants.csv",
    index=False
)

conn.close()

print("CSV exported!")