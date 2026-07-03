import time

from src.api import (
    get_challenger_players,
    get_match_ids,
    get_match_details,
    get_grandmaster_players,
    get_master_players
)

from src.transform import (
    players_to_dataframe,
    match_info_to_dataframe,
    participants_to_dataframe
)

from src.database import save_dataframe


data = get_challenger_players()

datasets = [
    get_challenger_players("euw1"),
    get_grandmaster_players("euw1"),
    get_master_players("euw1")
]

matches_saved = 0
unique_matches = set()

for data in datasets:

    print("\nPlayers found:")
    print(len(data["entries"]))

    players_df = players_to_dataframe(data)
    save_dataframe(players_df, "players")

    # цикл по игрокам находится ВНУТРИ цикла по датасетам
    for player in data["entries"][:20]:

        puuid = player["puuid"]

        match_ids = get_match_ids(
            puuid,
            count=10
        )

        time.sleep(1)

        for match_id in match_ids:

            if match_id in unique_matches:
                continue

            unique_matches.add(match_id)

            match = get_match_details(match_id)

            time.sleep(1)

            match_df = match_info_to_dataframe(match)
            participants_df = participants_to_dataframe(match)

            save_dataframe(match_df, "matches")
            save_dataframe(participants_df, "participants")

            matches_saved += 1

            print("Saved:", match_id)

print("\nUnique matches saved:")
print(matches_saved)