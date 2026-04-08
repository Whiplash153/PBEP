from app.repositories.user_repository import UserRepo
from app.repositories.vote_repository import VoteRepo
from app.repositories.proposal_repository import ProposalRepo

from app.models.proposal import Proposal
from app.models.vote import Vote
from app.models.user import User

from sqlalchemy.orm import Session

class ProposalService:
    def __init__(self, session: Session):
        self.session = session
        self.proposal_repo = ProposalRepo(session)
        self.user_repo = UserRepo(session)
        self.vote_repo = VoteRepo(session)
