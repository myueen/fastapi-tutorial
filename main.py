"""FastAPI main entrypoint file."""

from typing import Annotated, TypeAlias
from fastapi import FastAPI, Body, Depends
from models import GamePlay, GameResult
from services import GameService

app = FastAPI()


@app.post("/play")
def play(
    user_choice: Annotated[
        GamePlay,
        Body(description="User's choice of rock, paper, or scissors."),
    ],
) -> GameResult:
    # Here we construct a GameService *without* dependency injection...
    game_svc: GameService = GameService()
    return game_svc.play(user_choice)
