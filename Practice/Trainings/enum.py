from enum import Enum

class CartState(Enum):
    EMPTY = "empty"
    ACTIVE = "active"
    CHECKOUT = "checkout"
    ORDERED = "ordered"

ALLOWED_TRANSITIONS = {
    CartState.EMPTY: {CartState.ACTIVE},
    CartState.ACTIVE: {CartState.CHECKOUT},
    CartState.CHECKOUT: {CartState.ORDERED},
    CartState.ORDERED: set(),
}

class Cart:
    def __init__(self):
        self.state = CartState.EMPTY

    def change_state(self, new_state: CartState):
        allowed = ALLOWED_TRANSITIONS[self.state]

        if new_state not in allowed:
            raise ValueError(f"Cannot switch from {self.state.value} to {new_state.value}")

        self.state = new_state