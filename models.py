from enum import Enum
from datetime import datetime
from typing import Annotated, TypeAlias
from pydantic import BaseModel, Field


class Choice(str, Enum):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"


ChoiceField: TypeAlias = Annotated[
    Choice,
    Field(
        description="Choice of rock, paper, or scissors.",
        examples=["rock", "paper", "scissors"],
    ),
]


class GamePlay(BaseModel):
    user_choice: ChoiceField


class GameResult(BaseModel):
    timestamp: Annotated[datetime, Field(description="When the game was played.")]
    user_choice: ChoiceField
    api_choice: ChoiceField
    user_wins: Annotated[bool, Field(description="Did the user win the game?")]
