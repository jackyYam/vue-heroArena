import requests
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
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
                        for stat, value in powerstats.items():
                            if value == "null":
                                powerstats[stat] = random.randint(0, 50)
                            else:
                                powerstats[stat] = int(value)
                        powerstats["AS"] = random.randint(0, 10)
                        heroes.append(
                            {
                                "id": hero_id,
                                "name": hero_data["name"],
                                "powerstats": powerstats,
                                "alignment": hero_data["biography"][
                                    "alignment"
                                ],
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


@app.get("/teams")
async def get_superheros():
    return {"message": "Use the WebSocket endpoint to get progress updates."}
