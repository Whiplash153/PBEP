from enum import Enum

class CartState(Enum):
    EMPTY = "empty"
    ACTIVE = "active"
    CHECKOUT = "checkout"
    ORDERED = "ordered"