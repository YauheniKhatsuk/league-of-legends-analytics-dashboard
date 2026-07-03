import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect(
    "database/lol.db"
)

lp_query = """
SELECT
    CASE
        WHEN leaguePoints < 500 THEN '0-499'
        WHEN leaguePoints < 1000 THEN '500-999'
        WHEN leaguePoints < 1500 THEN '1000-1499'
        WHEN leaguePoints < 2000 THEN '1500-1999'
        ELSE '2000+'
    END AS lp_group,
    COUNT(*) AS players
FROM players
GROUP BY lp_group
ORDER BY lp_group
"""

df = pd.read_sql(
    lp_query,
    conn
)

print(df)

plt.figure(
    figsize=(8, 5)
)

plt.bar(
    df["lp_group"],
    df["players"]
)

plt.title(
    "Players Distribution by LP"
)

plt.xlabel(
    "LP Range"
)

plt.ylabel(
    "Number of Players"
)

plt.tight_layout()

plt.show()

champ_query = """
SELECT
    champion,
    COUNT(*) as games
FROM participants
GROUP BY champion
ORDER BY games DESC
LIMIT 10
"""
df = pd.read_sql(
    champ_query,
    conn
)

print(df)

plt.figure(figsize=(10,5))

plt.bar(
    df["champion"],
    df["games"]
)

plt.title(
    "Top 10 Most Played Champions"
)

plt.xlabel(
    "Champion"
)

plt.ylabel(
    "Games"
)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "reports/top_champions.png"
)

plt.show()

winrate_query = """
SELECT
    champion,
    COUNT(*) as games,
    ROUND(
        AVG(win) * 100,
        2
    ) as winrate
FROM participants
GROUP BY champion
HAVING games >= 50
ORDER BY winrate DESC
LIMIT 15
"""

winrate_df = pd.read_sql(
    winrate_query,
    conn
)

print("\nTOP WINRATE")
print(winrate_df)

plt.figure(figsize=(10,5))

plt.bar(
    winrate_df["champion"],
    winrate_df["winrate"]
)

plt.title(
    "Top 15 Champions by Win Rate"
)

plt.xlabel(
    "Champion"
)

plt.ylabel(
    "Win Rate (%)"
)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "reports/top_winrate.png"
)

plt.show()

kda_query = """
SELECT
    champion,
    COUNT(*) as games,
    ROUND(
        AVG(
            (kills + assists) * 1.0 /
            CASE
                WHEN deaths = 0 THEN 1
                ELSE deaths
            END
        ),
        2
    ) as avg_kda
FROM participants
GROUP BY champion
HAVING games >= 10
ORDER BY avg_kda DESC
LIMIT 10
"""

kda_df = pd.read_sql(
    kda_query,
    conn
)

print("\nTOP KDA")
print(kda_df)

plt.figure(figsize=(10,5))

plt.bar(
    kda_df["champion"],
    kda_df["avg_kda"]
)

plt.title(
    "Top 10 Champions by Average KDA"
)

plt.xlabel(
    "Champion"
)

plt.ylabel(
    "Average KDA"
)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "reports/top_kda.png"
)

plt.show()

conn.close()