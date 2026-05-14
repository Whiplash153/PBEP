import threading

from app.services.proposal_service import ProposalService
from tests.reserve_db_session import SessionLocal

from app.models.vote import Vote
from app.models.participant import Participant
from app.models.proposal import Proposal
from app.models.user import User

#CLEAR DB
def _clear_db():
    session = SessionLocal()
    session.query(Vote).delete()
    session.query(Participant).delete()
    session.query(Proposal).delete()
    session.query(User).delete()
    session.commit()
    session.close()

def same_time_voting():

    #CLEAR DB
    _clear_db()

