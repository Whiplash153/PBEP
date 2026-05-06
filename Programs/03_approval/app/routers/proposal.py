from fastapi import APIRouter, HTTPException
from app.services.proposal_service import ProposalService
from app.db.session import SessionLocal

from app.schemas.proposal import ProposalCreateSchema, ProposalResponseSchema, ProposalResultSchema
from app.schemas.vote import VoteCreateSchema, VoteResponseSchema

router = APIRouter()

@router.post("/proposals", response_model=ProposalResponseSchema)
def create_proposal(data: ProposalCreateSchema):
    session = SessionLocal()
    service = ProposalService(session)
    proposal = service.create_proposal(data.title, data.description, data.author_id, data.participant_ids)
    return ProposalResponseSchema(
        id=proposal.id,
        title=proposal.title,
        description=proposal.description,
        author_id=proposal.author_id,
        status=proposal.status
    )

@router.get("/proposals/{proposal_id}", response_model=ProposalResponseSchema)
def get_proposal_by_id(proposal_id):
    session = SessionLocal()
    service = ProposalService(session)
    proposal = service.get_proposal(proposal_id=proposal_id)

    return ProposalResponseSchema(
        id=proposal.id,
        title=proposal.title,
        description=proposal.description,
        author_id=proposal.author_id,
        status=proposal.status
    )

@router.post("/votes", response_model=VoteResponseSchema)
def create_vote(data: VoteCreateSchema):
    session = SessionLocal()
    service = ProposalService(session)
    vote = service.create_vote(data.value, data.proposal_id, data.user_id)
    proposal = service.get_proposal(data.proposal_id)
    return VoteResponseSchema(
        value=vote.value,
        user_id=vote.user_id,
        proposal_id=vote.proposal_id,
        status=proposal.status
    )

@router.get("/proposals/{proposal_id}/result", response_model=ProposalResultSchema)
def get_proposal_result(proposal_id):
    session = SessionLocal()
    service = ProposalService(session)
    proposal = service.get_proposal(proposal_id=proposal_id)

    return ProposalResultSchema(
        status=proposal.status
    )
