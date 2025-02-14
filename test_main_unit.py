    # Verify how the service was used
    mock_service.play.assert_called_once_with(GamePlay(user_choice=Choice.rock))