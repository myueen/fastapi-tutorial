from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_play_route_integration():
    """Test that the /play endpoint handles basic gameplay correctly."""
    response = client.post("/play", json={"user_choice": "rock"})

    # Verify HTTP-level details
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    # Verify response structure
    data = response.json()
    assert "user_choice" in data
    assert "api_choice" in data
    assert "user_wins" in data
    assert "timestamp" in data

    # Verify data types and constraints
    assert data["user_choice"] == "rock"  # Our input is preserved
    assert data["api_choice"] in ["rock", "paper", "scissors"]
    assert isinstance(data["user_wins"], bool)