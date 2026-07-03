import os
import requests

from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Получаем API ключ
API_KEY = os.getenv("RIOT_API_KEY")

print("Первые символы ключа:", API_KEY[:12])

print("Ключ найден:", API_KEY is not None)

url = (
    "https://euw1.api.riotgames.com/"
    "lol/league/v4/challengerleagues/"
    "by-queue/RANKED_SOLO_5x5"
)

headers = {
    "X-Riot-Token": API_KEY
}

response = requests.get(
    url,
    headers=headers
)

print("Статус:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("Tier:", data["tier"])
    print("Players:", len(data["entries"]))

    for player in data["entries"][:5]:
        print(
            player["leaguePoints"],
            player["wins"],
            player["losses"]
        )

else:
    print(response.text)
