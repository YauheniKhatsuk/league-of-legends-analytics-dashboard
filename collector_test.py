from src.api import (
    get_challenger_players,
    get_match_ids,
    get_match_details
)

data = get_challenger_players()

total_matches = 0

for player in data["entries"][:3]:

    puuid = player["puuid"]

    print("\nPLAYER:")
    print(puuid)

    match_ids = get_match_ids(
        puuid,
        count=3
    )

    for match_id in match_ids:

        print("\nDownloading:", match_id)

        match = get_match_details(
            match_id
        )

        total_matches += 1

print("\nВсего матчей скачано:")
print(total_matches)

from src.api import (
    get_grandmaster_players,
    get_master_players
)

grandmaster = get_grandmaster_players()

print(
    "Grandmaster:",
    len(grandmaster["entries"])
)

master = get_master_players()

print(
    "Master:",
    len(master["entries"])
)