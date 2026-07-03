import pandas as pd


def participants_to_dataframe(match):

    participants = (
        match["info"]["participants"]
    )

    match_id = (
        match["metadata"]["matchId"]
    )

    game_duration = (
        match["info"]["gameDuration"]
    )

    game_mode = (
        match["info"]["gameMode"]
    )

    rows = []

    for player in participants:

        rows.append({

            "champion":
                player["championName"],

            "kills":
                player["kills"],

            "deaths":
                player["deaths"],

            "assists":
                player["assists"],

            "win":
                player["win"],

            "role":
                player["teamPosition"],
                
            "puuid":
                player["puuid"],

            "match_id":
                match_id,

            "game_duration":
                game_duration,

            "game_mode":
                game_mode

        })

    return pd.DataFrame(rows)


def players_to_dataframe(data):

    rows = []

    for player in data["entries"]:

        rows.append({

            "puuid":
                player["puuid"],

            "leaguePoints":
                player["leaguePoints"],

            "wins":
                player["wins"],

            "losses":
                player["losses"]

        })

    return pd.DataFrame(rows)


def match_info_to_dataframe(match):

    row = {

        "match_id":
            match["metadata"]["matchId"],

        "game_duration":
            match["info"]["gameDuration"],

        "game_mode":
            match["info"]["gameMode"]

    }

    return pd.DataFrame([row])