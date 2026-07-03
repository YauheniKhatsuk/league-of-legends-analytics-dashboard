import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/lol.db"
)

#Распределение игроков по LP

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

lp_df = pd.read_sql(lp_query, conn)

print("\nLP DISTRIBUTION")
print(lp_df)

#самые популярные чемпионы

champ_query = """
SELECT
    champion,
    COUNT(*) as games
FROM participants
GROUP BY champion
ORDER BY games DESC
LIMIT 10
"""

champ_df = pd.read_sql(champ_query, conn)

print("\nTOP CHAMPIONS")
print(champ_df)

#средний kda по чемпионам

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

kda_df = pd.read_sql(kda_query, conn)

print("\nTOP KDA")
print(kda_df)

#топ 15 чемпионов по винрейту

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

#средняя длительность побед и поражений

duration_query = """
SELECT
    ROUND(
        AVG(game_duration)/60,
        2
    ) AS avg_minutes
FROM matches
"""

duration_df = pd.read_sql(
    duration_query,
    conn
)

print("\nMATCH DURATION VS WIN")
print(duration_df)

conn.close()