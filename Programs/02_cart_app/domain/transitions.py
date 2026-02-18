from states import CartState

ALLOWED_TRANSITIONS = {
    CartState.EMPTY: {CartState.ACTIVE},
    CartState.ACTIVE: {CartState.CHECKOUT},
    CartState.CHECKOUT: {CartState.ORDERED},
    CartState.ORDERED: set(),
}