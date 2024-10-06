from pydantic import BaseModel
import requests
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from hero import Hero, HeroFull, parse_hero, Team, get_team_alignment
from typing import List
import os
import random
import asyncio

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.websocket("/ws/get-heroes")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            if data == "start":
                await websocket.send_text("Progress: 0%")
                api_key = os.getenv("SUPERHERO_API_KEY")
                base_url = f"https://www.superheroapi.com/api/{api_key}/"

                # Generate 10 non-repetitive random IDs between 1 and 731
                hero_ids = random.sample(range(1, 732), 10)

                heroes = []
                total_heroes = len(hero_ids)
                for index, hero_id in enumerate(hero_ids):
                    url = f"{base_url}{hero_id}"
                    response = requests.get(url)
                    if response.status_code == 200:
                        hero_data = response.json()
                        powerstats = hero_data.get("powerstats", {})
                        hero_data["biography"] = {
                            k.replace("-", "_"): v
                            for k, v in hero_data["biography"].items()
                        }
                        for stat, value in powerstats.items():
                            if value == "null":
                                powerstats[stat] = random.randint(0, 50)
                            else:
                                powerstats[stat] = int(value)
                        powerstats["AS"] = random.randint(0, 10)
                        alignment = hero_data["biography"].get("alignment")
                        if alignment == "-":
                            alignment = "neutral"
                        heroes.append(
                            {
                                "id": hero_id,
                                "name": hero_data["name"],
                                "powerstats": powerstats,
                                "alignment": alignment,
                                "biography": hero_data["biography"],
                                "image": hero_data["image"]["url"],
                            }
                        )
                    # Send progress update
                    progress = int((index + 1) / total_heroes * 100)
                    await websocket.send_text(f"{progress}")
                    await asyncio.sleep(
                        0.1
                    )  # Simulate delay for demonstration

                await websocket.send_text(f"{progress}")
                await websocket.send_json({"heroes": heroes})
                break
    except Exception as e:
        print(f"WebSocket connection closed: {e}")


class HeroesRequest(BaseModel):
    heroes: List[Hero]


@app.post("/teams")
async def create_teams(request: HeroesRequest):
    heroes = request.heroes
    random.shuffle(heroes)
    mid_index = len(heroes) // 2
    team1_heroes = heroes[:mid_index]
    team2_heroes = heroes[mid_index:]

    team1_alignment = get_team_alignment(
        [parse_hero(hero, hero.alignment) for hero in team1_heroes]
    )
    team2_alignment = get_team_alignment(
        [parse_hero(hero, hero.alignment) for hero in team2_heroes]
    )

    parsed_team1 = [parse_hero(hero, team1_alignment) for hero in team1_heroes]
    parsed_team2 = [parse_hero(hero, team2_alignment) for hero in team2_heroes]

    return {
        "team1": Team(alignment=team1_alignment, heroes=parsed_team1),
        "team2": Team(alignment=team2_alignment, heroes=parsed_team2),
    }
