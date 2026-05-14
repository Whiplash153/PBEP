from sqlalchemy.orm import Session
from app.models.proposal import Proposal

class ProposalRepo:
    def __init__(self, session: Session):
        self.session = session

    def add(self, proposal: Proposal):
        self.session.add(proposal)

    def get_by_id(self, proposal_id):
        result = self.session.query(Proposal).filter(Proposal.id == proposal_id).first()
        return result

    def locked_get_by_id(self, proposal_id):
        result = self.session.query(Proposal).filter(Proposal.id == proposal_id).with_for_update().first()
        return result

    def delete(self, proposal):
        self.session.delete(proposal)