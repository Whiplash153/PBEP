class DomainError(Exception):
    pass

class InvalidTransitionError(DomainError):
    pass

class OperationNotAllowedError(DomainError):
    pass

class InvalidStateError(DomainError):
    pass

