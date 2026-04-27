import pytest

from app.services.proposal_service import ProposalService
from app.models.user import User
from app.repositories.user_repository import UserRepo
from app.core.errors import DuplicateParticipantsError, EmptyParticipantsError

def test_create_user(session):

    #SETUP
    user = User()
    user.name = "Henry"
    user.email = "test@test.com"

    session.add(user)
    session.commit()

    #TEST
    user_repo = UserRepo(session)
    the_user = user_repo.get_by_id(user.id)

    assert the_user.name == "Henry"
    assert the_user.email == "test@test.com"

def test_create_proposal(session):

    #SETUP
    user1 = User()
    user1.name = "A"
    user1.email = "a@test.com"

    user2 = User()
    user2.name = "B"
    user2.email = "b@test.com"

    user3 = User()
    user3.name = "C"
    user3.email = "c@test.com"

    session.add_all([user1, user2, user3])
    session.commit()

    #TEST
    service = ProposalService(session)
    proposal = service.create_proposal("proposal_test", "good", user1.id,
                            [user1.id, user2.id, user3.id])

    assert proposal.title == "proposal_test"
    assert proposal.description == "good"
    assert proposal.author_id == user1.id
    assert proposal.status == "draft"

    actual_ids = [participant.user_id for participant in proposal.participants]
    expected_ids = [user1.id, user2.id, user3.id]
    assert set(actual_ids) == set(expected_ids)

def test_proposal_duplicate_error(session):

    #SETUP
    user1 = User()
    user1.name = "A"
    user1.email = "a@test.com"

    user2 = User()
    user2.name = "B"
    user2.email = "b@test.com"

    session.add_all([user1, user2])
    session.commit()

    #TEST
    service = ProposalService(session)
    with pytest.raises(DuplicateParticipantsError):
        service.create_proposal("proposal_test", "good", user1.id,
                                [user1.id, user2.id, user2.id])

def test_proposal_participants_empty(session):

    #SETUP
    user1 = User()
    user1.name = "A"
    user1.email = "a@test.com"

    session.add([user1])
    session.commit()

    #TEST
    service = ProposalService(session)
    with pytest.raises(EmptyParticipantsError):
        service.create_proposal("proposal_test", "good", user1.id,
                                [])

