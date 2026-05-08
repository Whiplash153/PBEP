from app.repositories.user_repository import UserRepo
from app.repositories.vote_repository import VoteRepo
from app.repositories.proposal_repository import ProposalRepo
from app.repositories.participant_repository import ParticipantRepo

from app.models.proposal import Proposal
from app.models.vote import Vote
from app.models.participant import Participant

from sqlalchemy.orm import Session

from app.models.enums import ProposalStatus
from app.core.errors import (
    ProposalNotFoundError,
    NotParticipantError,
    AlreadyVotedError,
    InvalidProposalStatusError,
    NotAuthorError,
    UserNotFoundError,
    EmptyParticipantsError,
    DuplicateParticipantsError,
)

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
            raise UserNotFoundError

        #PARTICIPANT_IDS CHECK
        if not participant_ids:
            raise EmptyParticipantsError

        if len(participant_ids) != len(set(participant_ids)):
            raise DuplicateParticipantsError

        participants_list = []
        for participant_id in participant_ids:
            user = self.user_repo.get_by_id(participant_id)
            if not user:
                raise UserNotFoundError
            participants_list.append(user)

        #CREATE PROPOSAL
        new_proposal = Proposal(
            title=title,
            description=description,
            author_id=author_id,
            status=ProposalStatus.DRAFT
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
            raise ProposalNotFoundError

        #AUTHOR CHECK
        if proposal.author_id != author_id:
            raise NotAuthorError

        #STATUS CHECK
        if proposal.status != ProposalStatus.DRAFT:
            raise InvalidProposalStatusError

        #STATUS CHANGE
        proposal.status = ProposalStatus.VOTING

        #COMMIT, REFRESH AND RETURN PROPOSAL
        self.session.commit()
        self.session.refresh(proposal)
        return proposal

    def delete_proposal(self, proposal_id, author_id):

        #FIND PROPOSAL
        proposal = self.proposal_repo.get_by_id(proposal_id)
        if not proposal:
            raise ProposalNotFoundError

        #AUTHOR CHECK
        if proposal.author_id != author_id:
            raise NotAuthorError

        #STATUS CHECK
        if proposal.status != ProposalStatus.DRAFT:
            raise InvalidProposalStatusError

        #DELETE
        self.proposal_repo.delete(proposal)

        #COMMIT AND RETURN PROPOSAL
        self.session.commit()
        return proposal

    def create_vote(self, proposal_id, user_id, value):

        #FIND PROPOSAL
        proposal = self.proposal_repo.get_by_id(proposal_id)
        if not proposal:
            raise ProposalNotFoundError

        #IS USER PARTICIPANT
        participant = self.participant_repo.get_by_user_and_proposal(user_id, proposal_id)
        if not participant:
            raise NotParticipantError

        #VOTE MADE CHECK
        existing_vote = self.vote_repo.get_by_user_and_proposal(user_id, proposal_id)
        if existing_vote:
            raise AlreadyVotedError

        #STATUS CHECK
        if proposal.status != ProposalStatus.VOTING:
            raise InvalidProposalStatusError

        #CREATE VOTE
        new_vote = Vote(
            proposal_id=proposal_id,
            user_id=user_id,
            value=value
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
            raise ProposalNotFoundError

        #AUTHOR CHECK
        if proposal.author_id != author_id:
            raise NotAuthorError

        #STATUS CHECK
        if proposal.status != ProposalStatus.VOTING:
            raise InvalidProposalStatusError

        #FINISH PROPOSAL
        self._finish_proposal(proposal.id)

        self.session.commit()
        return proposal

    def _finish_proposal(self, proposal_id):

        #FIND PROPOSAL
        proposal = self.proposal_repo.get_by_id(proposal_id)
        if not proposal:
            raise ProposalNotFoundError

        #STATUS CHECK
        if proposal.status != ProposalStatus.VOTING:
            raise InvalidProposalStatusError

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
            proposal.status = ProposalStatus.APPROVED
        else:
            proposal.status = ProposalStatus.REJECTED

    def get_proposal(self, proposal_id):

        #FIND PROPOSAL
        proposal = self.proposal_repo.get_by_id(proposal_id)
        if not proposal:
            raise ProposalNotFoundError

        return proposal

    def get_proposal_votes(self, proposal_id):

        #FIND PROPOSAL
        proposal = self.proposal_repo.get_by_id(proposal_id)
        if not proposal:
            raise ProposalNotFoundError

        proposal_votes = self.vote_repo.get_by_proposal_id(proposal_id)
        return proposal_votes

    def get_proposal_participants(self, proposal_id):

        #FIND PROPOSAL
        proposal = self.proposal_repo.get_by_id(proposal_id)
        if not proposal:
            raise ProposalNotFoundError

        proposal_participants = self.participant_repo.get_by_proposal_id(proposal_id)
        return proposal_participants






