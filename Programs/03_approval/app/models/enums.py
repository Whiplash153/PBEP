from enum import Enum

class ProposalStatus(Enum):
    DRAFT = "draft"
    VOTING = "voting"
    APPROVED = "approved"
    REJECTED = "rejected"
    DELETED = "deleted"