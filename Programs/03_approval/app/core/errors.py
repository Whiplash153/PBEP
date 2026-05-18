class BaseDomainError(Exception):
    pass

class ProposalNotFoundError(BaseDomainError):
    pass

class UserNotFoundError(BaseDomainError):
    pass

class NotParticipantError(BaseDomainError):
    pass

class AlreadyVotedError(BaseDomainError):
    pass

class InvalidProposalStatusError(BaseDomainError):
    pass

class NotAuthorError(BaseDomainError):
    pass

class InvalidVoteValueError(BaseDomainError):
    pass

class EmptyParticipantsError(BaseDomainError):
    pass

class DuplicateParticipantsError(BaseDomainError):
    pass

class VoteNotExistsError(BaseDomainError):
    pass