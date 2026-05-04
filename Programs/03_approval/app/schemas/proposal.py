from pydantic import BaseModel, Field
from app.models.enums import ProposalStatus

class ProposalCreateSchema(BaseModel):

    title: str = Field(min_length=2, max_length=50)
    description: str = Field(min_length=2, max_length=500)
    author_id: int
    participant_ids: list[int]

class ProposalResponseSchema(BaseModel):

    id: int
    title: str = Field(min_length=2, max_length=50)
    description: str = Field(min_length=2, max_length=500)
    author_id: int
    status: ProposalStatus
    