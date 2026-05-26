from app.main import app
from app.db.session import get_db
from app.models import Vote, Proposal, Participant, AuditLog

from tests.reserve_db_session import SessionLocal as TestSessionLocal

from fastapi.testclient import TestClient

client = TestClient(app)

# ==== GET TEST DB ====
# =====================

def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# ==== HELPERS ====
# =================

def _clear_db():
    session = TestSessionLocal()

    session.query(AuditLog).delete()
    session.query(Vote).delete()
    session.query(Participant).delete()
    session.query(Proposal).delete()

    session.commit()
    session.close()

# ==== TESTS ====
# ===============

def test_create_proposal():

    #CLEAR DB
    _clear_db()

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

def test_empty_participants():

    #CLEAR DB
    _clear_db()

    #DATA TO SEND
    payload = {
        "title": "Test proposal",
        "description": "Test description",
        "author_id": 1,
        "participant_ids": []
    }

    #HTTP-REQUEST
    response = client.post("/proposals", json=payload)

    #STATUS CODE CHECK
    assert response.status_code == 400

    #GET RESPONSE
    data = response.json()

    #RESPONSE DETAILS CHECK
    assert data["detail"] == "Participants list is empty"

def test_duplicate_participants():

    #CLEAR DB
    _clear_db()

    #DATA TO SEND
    payload = {
        "title": "Test proposal",
        "description": "Test description",
        "author_id": 1,
        "participant_ids": [1, 1]
    }

    #HTTP-REQUEST
    response = client.post("/proposals", json=payload)

    #STATUS CODE CHECK
    assert response.status_code == 400

    #GET RESPONSE
    data = response.json()

    #RESPONSE DETAILS CHECK
    assert data["detail"] == "Duplicate participants"

def test_user_not_found():

    #CLEAR DB
    _clear_db()

    #DATA TO SEND
    payload = {
        "title": "Test proposal",
        "description": "Test description",
        "author_id": 999,
        "participant_ids": [1, 2]
    }

    #HTTP-REQUEST
    response = client.post("/proposals", json=payload)

    #STATUS CODE CHECK
    assert response.status_code == 404

    #GET RESPONSE
    data = response.json()

    #RESPONSE DETAILS CHECK
    assert data["detail"] == "User not found"

def test_already_voted():

    #CLEAR DB
    _clear_db()

    #DATA TO SEND
    payload = {
        "title": "Test proposal",
        "description": "Test description",
        "author_id": 1,
        "participant_ids": [1, 2]
    }

    #MAKING PROPOSAL
    proposal_response = client.post("/proposals", json=payload)
    proposal_id = proposal_response.json()["id"]

    #START VOTING
    client.post(f"/proposals/{proposal_id}/start", json={"author_id": 1})

    #1st VOTE (GOOD)
    vote_payload = {
        "proposal_id": proposal_id,
        "user_id": 1,
        "value": "approve"
    }

    vote1 = client.post("/votes", json=vote_payload)
    assert vote1.status_code == 200

    #2nd VOTE (BAD)
    vote2 = client.post("/votes", json=vote_payload)
    assert vote2.status_code == 409

    data = vote2.json()
    assert data["detail"] == "User already voted"

def test_not_participant():

    #CLEAR DB
    _clear_db()

    #DATA TO SEND
    payload = {
        "title": "Test proposal",
        "description": "Test description",
        "author_id": 1,
        "participant_ids": [1, 2]
    }

    #MAKING PROPOSAL
    proposal_response = client.post("/proposals", json=payload)
    proposal_id = proposal_response.json()["id"]

    #START VOTING
    client.post(f"/proposals/{proposal_id}/start", json={"author_id": 1})

    #VOTE
    vote_payload = {
        "proposal_id": proposal_id,
        "user_id": 4,
        "value": "approve"
    }

    vote1 = client.post("/votes", json=vote_payload)
    assert vote1.status_code == 403

    data = vote1.json()
    assert data["detail"] == "User is not a participant"

def test_vote_after_finish():

    #CLEAR DB
    _clear_db()

    #DATA TO SEND
    payload = {
        "title": "Test proposal",
        "description": "Test description",
        "author_id": 1,
        "participant_ids": [1, 2]
    }

    #MAKING PROPOSAL
    proposal_response = client.post("/proposals", json=payload)
    proposal_id = proposal_response.json()["id"]

    #START VOTING
    client.post(f"/proposals/{proposal_id}/start", json={"author_id": 1})

    #VOTE
    vote_payload_1 = {
        "proposal_id": proposal_id,
        "user_id": 1,
        "value": "approve"
    }

    client.post("/votes", json=vote_payload_1)

    #FINISH VOTE
    client.post(f"/proposals/{proposal_id}/finish", json={"author_id": 1})

    #VOTE AGAIN
    vote_payload_2 = {
        "proposal_id": proposal_id,
        "user_id": 2,
        "value": "approve"
    }

    vote2 = client.post("/votes", json=vote_payload_2)
    assert vote2.status_code == 409

    data = vote2.json()
    assert data["detail"] == "Proposal in a wrong state"
