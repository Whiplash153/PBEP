from app.repositories.user_repository import UserRepo
from app.repositories.vote_repository import VoteRepo
from app.repositories.proposal_repository import ProposalRepo
from app.repositories.participant_repository import ParticipantRepo

from app.models.proposal import Proposal
from app.models.vote import Vote
from app.models.participant import Participant

from sqlalchemy.orm import Session

from app.models.enums import ProposalStatus

class ProposalService:
    def __init__(self, session: Session):
        self.session = session
        self.proposal_repo = ProposalRepo(session)
        self.user_repo = UserRepo(session)
        self.vote_repo = VoteRepo(session)
        self.participant_repo = ParticipantRepo(session)

    def create_proposal(self, title, description, author_id, participant_ids):

        #AUTHOR CHECK
        author = self.user_repo.get_by_id(author_id)
        if not author:
            raise ValueError

        #PARTICIPANT_IDS CHECK
        if not participant_ids:
            raise ValueError

        if len(participant_ids) != len(set(participant_ids)):
            raise ValueError

        participants_list = []
        for participant_id in participant_ids:
            user = self.user_repo.get_by_id(participant_id)
            if not user:
                raise ValueError
            participants_list.append(user)

        #CREATE PROPOSAL
        new_proposal = Proposal(
            title=title,
            description=description,
            author_id=author_id,
            status=ProposalStatus.DRAFT.value
        )

        #ADD PROPOSAL
        self.proposal_repo.add(new_proposal)
        
        #GET PROPOSAL ID
        self.session.flush()

        #CREATE PARTICIPANTS
        for user in participants_list:
            participant = Participant(
                proposal_id=new_proposal.id,
                user_id=user.id
            )
            self.participant_repo.add(participant)

        #COMMIT, REFRESH AND RETURN PROPOSAL
        self.session.commit()
        self.session.refresh(new_proposal)
        return new_proposal

    def start_voting(self, proposal_id, author_id):

        #FIND PROPOSAL
        proposal = self.proposal_repo.get_by_id(proposal_id)
        if not proposal:
            raise ValueError

        #AUTHOR CHECK
        if proposal.author_id != author_id:
            raise ValueError

        #STATUS CHECK
        if proposal.status != ProposalStatus.DRAFT.value:
            raise ValueError

        #STATUS CHANGE
        proposal.status = ProposalStatus.VOTING.value

        #COMMIT, REFRESH AND RETURN PROPOSAL
        self.session.commit()
        self.session.refresh(proposal)
        return proposal

    def delete_proposal(self, proposal_id, author_id):

        #FIND PROPOSAL
        proposal = self.proposal_repo.get_by_id(proposal_id)
        if not proposal:
            raise ValueError

        #AUTHOR CHECK
        if proposal.author_id != author_id:
            raise ValueError

        #STATUS CHECK
        if proposal.status != ProposalStatus.DRAFT.value:
            raise ValueError

        #DELETE
        self.proposal_repo.delete(proposal)

        #COMMIT AND RETURN PROPOSAL
        self.session.commit()
        return proposal

    def create_vote(self, proposal_id, user_id, value):

        #FIND PROPOSAL
        proposal = self.proposal_repo.get_by_id(proposal_id)
        if not proposal:
            raise ValueError

        #IS USER PARTICIPANT
        participant = self.participant_repo.get_by_user_and_proposal(user_id, proposal_id)
        if not participant:
            raise ValueError

        #VOTE MADE CHECK
        existing_vote = self.vote_repo.get_by_user_and_proposal(user_id, proposal_id)
        if existing_vote:
            raise ValueError

        #STATUS CHECK
        if proposal.status != ProposalStatus.VOTING.value:
            raise ValueError

        #VALUE CHECK
        if value not in ["approve", "reject"]:
            raise ValueError

        #CREATE VOTE
        new_vote = Vote(
            value=value,
            user_id=user_id,
            proposal_id=proposal_id
        )

        #SAVE VOTE
        self.vote_repo.add(new_vote)
        self.session.flush()

        #FINISH CHECK
        if self.vote_repo.votes_count(proposal_id) == self.participant_repo.participants_count(proposal_id):
            self._finish_proposal(proposal.id)

        self.session.commit()
        return new_vote

    def manual_finish(self, proposal_id, author_id):

        #FIND PROPOSAL
        proposal = self.proposal_repo.get_by_id(proposal_id)
        if not proposal:
            raise ValueError

        #AUTHOR CHECK
        if proposal.author_id != author_id:
            raise ValueError

        #STATUS CHECK
        if proposal.status != ProposalStatus.VOTING.value:
            raise ValueError

        #FINISH PROPOSAL
        self._finish_proposal(proposal.id)

        self.session.commit()
        return proposal

    def _finish_proposal(self, proposal_id):

        #FIND PROPOSAL
        proposal = self.proposal_repo.get_by_id(proposal_id)
        if not proposal:
            raise ValueError

        #STATUS CHECK
        if proposal.status != ProposalStatus.VOTING.value:
            raise ValueError

        #APPROVE AND REJECT VOTES COUNT
        all_votes = self.vote_repo.get_by_proposal_id(proposal_id)

        approve_count = 0
        reject_count = 0
        for vote in all_votes:
            if vote.value == "approve":
                approve_count += 1
            else:
                reject_count += 1

        #SET PROPOSAL STATUS
        if approve_count > reject_count:
            proposal.status = ProposalStatus.APPROVED.value
        else:
            proposal.status = ProposalStatus.REJECTED.value







