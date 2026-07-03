from src.api import (
    get_challenger_players,
    get_match_ids,
    get_match_details
)

from src.transform import (
    players_to_dataframe,
    match_info_to_dataframe,
    participants_to_dataframe
)

from src.database import save_dataframe

from src.api import get_summoner_by_puuid

# Получаем игроков
data = get_challenger_players()

# Берём первого игрока
puuid = data["entries"][0]["puuid"]

# Получаем список матчей
match_ids = get_match_ids(
    puuid,
    count=1
)

print("\nMatch ID:")
print(match_ids[0])

summoner = get_summoner_by_puuid(
    puuid
)

print("\nSUMMONER:")
print(summoner)


# Получаем детали матча
match = get_match_details(
    match_ids[0]
)

# Создаём DataFrame
players_df = players_to_dataframe(data)

match_df = match_info_to_dataframe(match)

participants_df = participants_to_dataframe(match)

print("\nPLAYERS:")
print(players_df.head())

print("\nMATCH:")
print(match_df.head())

print("\nPARTICIPANTS:")
print(participants_df.head())

save_dataframe(
    players_df,
    "players"
)

save_dataframe(
    match_df,
    "matches"
)

save_dataframe(
    participants_df,
    "participants"
)