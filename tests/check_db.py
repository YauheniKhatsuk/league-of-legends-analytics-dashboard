import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/lol.db"
)

print(
    pd.read_sql(
        "SELECT * FROM participants LIMIT 5",
        conn
    )
)

conn.close()