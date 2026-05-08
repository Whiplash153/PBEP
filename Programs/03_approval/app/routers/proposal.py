from fastapi import APIRouter
from app.services.proposal_service import ProposalService
from app.db.session import SessionLocal

from app.schemas.proposal import (
    ProposalCreateSchema,
    ProposalResponseSchema,
    ProposalResultSchema,
    StartProposalSchema,
    FinishProposalSchema
)
from app.schemas.vote import VoteCreateSchema, VoteResponseSchema

router = APIRouter()

@router.post("/proposals", response_model=ProposalResponseSchema)
def create_proposal(data: ProposalCreateSchema):
    session = SessionLocal()

    try:
        service = ProposalService(session)
        proposal = service.create_proposal(data.title, data.description, data.author_id, data.participant_ids)

        return ProposalResponseSchema(
            id=proposal.id,
            title=proposal.title,
            description=proposal.description,
            author_id=proposal.author_id,
            status=proposal.status
        )
    finally:
        session.close()

@router.get("/proposals/{proposal_id}", response_model=ProposalResponseSchema)
def get_proposal_by_id(proposal_id):
    session = SessionLocal()

    try:
        service = ProposalService(session)
        proposal = service.get_proposal(proposal_id=proposal_id)

        return ProposalResponseSchema(
            id=proposal.id,
            title=proposal.title,
            description=proposal.description,
            author_id=proposal.author_id,
            status=proposal.status
        )
    finally:
        session.close()

@router.post("/votes", response_model=VoteResponseSchema)
def create_vote(data: VoteCreateSchema):
    session = SessionLocal()

    try:
        service = ProposalService(session)
        vote = service.create_vote(data.proposal_id, data.user_id, data.value)
        proposal = service.get_proposal(data.proposal_id)

        return VoteResponseSchema(
            proposal_id=vote.proposal_id,
            user_id=vote.user_id,
            value=vote.value,
            status=proposal.status
        )
    finally:
        session.close()

@router.get("/proposals/{proposal_id}/result", response_model=ProposalResultSchema)
def get_proposal_result(proposal_id):
    session = SessionLocal()

    try:
        service = ProposalService(session)
        proposal = service.get_proposal(proposal_id=proposal_id)

        return ProposalResultSchema(
            status=proposal.status
        )
    finally:
        session.close()

@router.post("/proposals/{proposal_id}/start", response_model=ProposalResponseSchema)
def start_proposal(proposal_id, data: StartProposalSchema):
    session = SessionLocal()

    try:
        service = ProposalService(session)
        proposal = service.start_voting(proposal_id=proposal_id, author_id=data.author_id)

        return ProposalResponseSchema(
            id=proposal.id,
            title=proposal.title,
            description=proposal.description,
            author_id=proposal.author_id,
            status=proposal.status
        )
    finally:
        session.close()


@router.post("/proposals/{proposal_id}/finish", response_model=ProposalResponseSchema)
def finish_proposal(proposal_id, data: FinishProposalSchema):
    session = SessionLocal()

    try:
        service = ProposalService(session)
        proposal = service.manual_finish(proposal_id=proposal_id, author_id=data.author_id)

        return ProposalResponseSchema(
            id=proposal.id,
            title=proposal.title,
            description=proposal.description,
            author_id=proposal.author_id,
            status=proposal.status
        )
    finally:
        session.close()
