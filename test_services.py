from unittest.mock import MagicMock
from services import GameService
from models import Choice, GamePlay, GameResult
from datetime import datetime, UTC


def create_mock_game_service(choice_to_return: Choice) -> GameService:
    """Create a GameService with a mocked _random_choice method"""
    service = GameService()
    service._random_choice = MagicMock(return_value=choice_to_return)
    return service


def test_game_service_rock_beats_scissors():
    # Create a service that will return scissors
    service = create_mock_game_service(Choice.scissors)
    result = service.play(GamePlay(user_choice=Choice.rock))

    assert result.user_choice == Choice.rock
    assert result.api_choice == Choice.scissors
    assert result.user_wins is True
    service._random_choice.assert_called_once()


def test_game_service_scissors_loses_to_rock():
    service = create_mock_game_service(Choice.rock)
    result = service.play(GamePlay(user_choice=Choice.scissors))

    assert result.user_choice == Choice.scissors
    assert result.api_choice == Choice.rock
    assert result.user_wins is False
    service._random_choice.assert_called_once()


def test_game_service_draw():
    service = create_mock_game_service(Choice.paper)
    result = service.play(GamePlay(user_choice=Choice.paper))

    assert result.user_choice == Choice.paper
    assert result.api_choice == Choice.paper
    assert result.user_wins is False  # Draws count as API wins
    service._random_choice.assert_called_once()


def test_game_service_all_combinations():
    """Test all possible game combinations systematically"""
    # Define all possible combinations and expected results
    test_cases = [
        (Choice.rock, Choice.scissors, True),  # Rock beats scissors
        (Choice.rock, Choice.paper, False),  # Rock loses to paper
        (Choice.rock, Choice.rock, False),  # Rock ties rock (API wins)
        (Choice.paper, Choice.rock, True),  # Paper beats rock
        (Choice.paper, Choice.scissors, False),  # Paper loses to scissors
        (Choice.paper, Choice.paper, False),  # Paper ties paper (API wins)
        (Choice.scissors, Choice.paper, True),  # Scissors beats paper
        (Choice.scissors, Choice.rock, False),  # Scissors loses to rock
        (Choice.scissors, Choice.scissors, False),  # Scissors ties scissors (API wins)
    ]

    for user_choice, api_choice, expected_win in test_cases:
        # Create a service that will return the API choice we want to test
        service = create_mock_game_service(api_choice)
        result = service.play(GamePlay(user_choice=user_choice))

        assert result.user_choice == user_choice
        assert result.api_choice == api_choice
        assert result.user_wins == expected_win, (
            f"Failed when user played {user_choice.value} "
            f"against API's {api_choice.value}"
        )
        service._random_choice.assert_called_once()
