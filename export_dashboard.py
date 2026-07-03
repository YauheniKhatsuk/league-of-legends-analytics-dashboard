import sqlite3
import pandas as pd

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

df.to_csv(
    "reports/lp_distribution.csv",
    index=False
)

print("lp_distribution.csv exported")

champ_query = """
SELECT
    champion,
    COUNT(*) AS games
FROM participants
GROUP BY champion
ORDER BY games DESC
LIMIT 10
"""

df = pd.read_sql(
    champ_query,
    conn
)

df.to_csv(
    "reports/top_champions.csv",
    index=False
)

print("top_champions.csv exported")

kda_query = """
SELECT
    champion,
    COUNT(*) AS games,
    ROUND(
        AVG(
            (kills + assists) * 1.0 /
            CASE
                WHEN deaths = 0 THEN 1
                ELSE deaths
            END
        ),
        2
    ) AS avg_kda
FROM participants
GROUP BY champion
HAVING games >= 10
ORDER BY avg_kda DESC
LIMIT 10
"""

df = pd.read_sql(
    kda_query,
    conn
)

df.to_csv(
    "reports/top_kda.csv",
    index=False
)

print("top_kda.csv exported")

winrate_query = """
SELECT
    champion,
    COUNT(*) AS games,
    ROUND(
        AVG(win) * 100,
        2
    ) AS winrate
FROM participants
GROUP BY champion
HAVING games >= 50
ORDER BY winrate DESC
LIMIT 15
"""

df = pd.read_sql(
    winrate_query,
    conn
)

df.to_csv(
    "reports/top_winrate.csv",
    index=False
)

print("top_winrate.csv exported")

duration_query = """
SELECT
    ROUND(AVG(game_duration)/60,2) AS avg_minutes
FROM matches
"""

df = pd.read_sql(
    duration_query,
    conn
)

df.to_csv(
    "reports/match_duration.csv",
    index=False
)

print("match_duration.csv exported")

champion_query = """
SELECT
    champion,
    COUNT(*) AS games,

    ROUND(
        AVG(win) * 100,
        2
    ) AS winrate,

    ROUND(
        AVG(
            (kills + assists) * 1.0 /
            CASE
                WHEN deaths = 0 THEN 1
                ELSE deaths
            END
        ),
        2
    ) AS avg_kda

FROM participants

GROUP BY champion

HAVING COUNT(*) >= 10

ORDER BY games DESC;
"""

champion_stats = pd.read_sql(
    champion_query,
    conn
)

champion_stats.to_csv(
    "reports/champion_stats.csv",
    index=False
)

conn.close()