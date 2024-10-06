# vue-heroArena
Hero Arena app written in Vue, used for a job interview

# Frontend
Written in Vue.js, using Tailwind and shadcn as components library and styling options
To run 
```
pnpm install
pnpm run start
```
Bonus:
- Websocket connection for hero assembling process
- Darkmode

Considerations:
- On the team display phase, you can regenerate 2 teams from the obtained 10 heros, in order to make the battler more interesting
- During the game, you can choose either autoplay (autoplay button) or step to step (take turn button)

# Backend

Developed in fastapi, to run:

```
source .venv/bin/activate
pip install -r requirements.txt
fastapi dev main.py
```

Endpoints:
- ws://localhost:8000/ws/get-heroes:

    Websocket endpoint that streamlize the process of getting 10 random hero from [Superhero API](https://www.superheroapi.com/index.html)

- Post: http://127.0.0.1:8000/teams

    Endpoint that receives a list of heros and return 2 teams of processed hero according to requirement
