from datetime import datetime
from random import choice as random_choice
from models import GamePlay, GameResult, Choice

_db: list[GameResult] = []


class GameService:
    """Service for processing game plays.

    This class provides functionality to simulate a game between a user and the API.
    """

    def play(self, gameplay: GamePlay) -> GameResult:
        """Play a game round.

        Args:
            gameplay (GamePlay): An object encapsulating the user's choice.

        Returns:
            GameResult: The outcome of the game including user and API choices, and win flag.
        """
        api_choice: Choice = self._random_choice()

        result = GameResult(
            timestamp=datetime.now(),
            user_choice=gameplay.user_choice,
            api_choice=api_choice,
            user_wins=self._does_user_win(gameplay.user_choice, api_choice),
        )
        _db.append(result)
        return result

    def _random_choice(self) -> Choice:
        """Select a random choice for the API.

        Returns:
            Choice: A randomly chosen game option.
        """
        return random_choice(list(Choice))

    def _does_user_win(self, user_choice: Choice, api_choice: Choice) -> bool:
        """Determine if the user wins based on choices.

        Args:
            user_choice (Choice): The user's chosen option.
            api_choice (Choice): The API's chosen option.

        Returns:
            bool: True if the user wins, False otherwise.
        """
        result: tuple[Choice, Choice] = (user_choice, api_choice)
        winning_results: set[tuple[Choice, Choice]] = {
            (Choice.rock, Choice.scissors),
            (Choice.paper, Choice.rock),
            (Choice.scissors, Choice.paper),
        }
        return result in winning_results

    def get_results(self) -> list[GameResult]:
        """Get all game results.

        Returns:
            list[GameResult]: A list of all game results.
        """
        return _db
