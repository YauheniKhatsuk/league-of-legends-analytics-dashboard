import os
from pathlib import Path

import requests
from dotenv import load_dotenv


# Ищем .env в корне проекта
env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(env_path)


API_KEY = os.getenv("RIOT_API_KEY")

print("API_KEY loaded:", API_KEY is not None)


HEADERS = {
    "X-Riot-Token": API_KEY
}


def get_challenger_players(region="euw1"):

    url = (
        f"https://{region}.api.riotgames.com/"
        "lol/league/v4/challengerleagues/"
        "by-queue/RANKED_SOLO_5x5"
    )

    response = requests.get(
        url,
        headers=HEADERS
    )

    print("Status:", response.status_code)

    response.raise_for_status()

    return response.json()



def get_match_ids(
        puuid,
        region="europe",
        start=0,
        count=20
):

    url = (
        f"https://{region}.api.riotgames.com/"
        f"lol/match/v5/matches/by-puuid/{puuid}/ids"
    )


    params = {
        "start": start,
        "count": count
    }


    response = requests.get(
        url,
        headers=HEADERS,
        params=params
    )


    print("Match API status:", response.status_code)


    response.raise_for_status()


    return response.json()



def get_match_details(
        match_id,
        region="europe"
):

    url = (
        f"https://{region}.api.riotgames.com/"
        f"lol/match/v5/matches/{match_id}"
    )


    response = requests.get(
        url,
        headers=HEADERS
    )


    print(
        "Match details status:",
        response.status_code
    )


    response.raise_for_status()


    return response.json()

def get_summoner_by_puuid(
    puuid,
    region="euw1"
):
    url = (
        f"https://{region}.api.riotgames.com/"
        f"lol/summoner/v4/summoners/by-puuid/{puuid}"
    )

    response = requests.get(
        url,
        headers=HEADERS
    )

    print(
        "Summoner API status:",
        response.status_code
    )

    response.raise_for_status()

    return response.json()

def get_grandmaster_players(region="euw1"):

    url = (
        f"https://{region}.api.riotgames.com/"
        "lol/league/v4/grandmasterleagues/"
        "by-queue/RANKED_SOLO_5x5"
    )

    response = requests.get(
        url,
        headers=HEADERS
    )

    print(
        "Grandmaster status:",
        response.status_code
    )

    response.raise_for_status()

    return response.json()

def get_master_players(region="euw1"):

    url = (
        f"https://{region}.api.riotgames.com/"
        "lol/league/v4/masterleagues/"
        "by-queue/RANKED_SOLO_5x5"
    )

    response = requests.get(
        url,
        headers=HEADERS
    )

    print(
        "Master status:",
        response.status_code
    )

    response.raise_for_status()

    return response.json()   


