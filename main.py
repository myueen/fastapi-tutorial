"""FastAPI main entrypoint file."""

from typing import Annotated, TypeAlias
from fastapi import FastAPI, Body, Depends
from models import GamePlay, GameResult
from services import GameService

app = FastAPI()

GameServiceDI: TypeAlias = Annotated[GameService, Depends()]


@app.post("/play")
def play(
    user_choice: Annotated[
        GamePlay,
        Body(description="User's choice of rock, paper, or scissors."),
    ],
    game_svc: GameServiceDI,
) -> GameResult:
    return game_svc.play(user_choice)


@app.get("/results")
def log(game_svc: GameServiceDI) -> list[GameResult]:
    return game_svc.get_results()
