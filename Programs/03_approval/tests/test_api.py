from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_proposal():

    #DATA TO SEND
    payload = {
        "title": "Test proposal",
        "description": "Test description",
        "author_id": 1,
        "participant_ids": [1, 2]
    }

    #HTTP-REQUEST
    response = client.post("/proposals", json=payload)

    #STATUS CODE CHECK
    assert response.status_code == 200

    #GET RESPONSE
    data = response.json()

    #RESPONSE DETAILS CHECK
    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["author_id"] == payload["author_id"]

    #STATUS CHECK
    assert data["status"] == "draft"

