from domain.states import CartState
from domain.errors import OperationNotAllowedError


class Cart:
    def __init__(self, id):
        self.id = id
        self.state = CartState.EMPTY
        self.items = []

    def add_item(self, item):
        if self.state not in (CartState.EMPTY, CartState.ACTIVE):
            raise OperationNotAllowedError("Cannot add item in this state")

        self.items.append(item)

        if self.state == CartState.EMPTY:
            self.state = CartState.ACTIVE

    def remove_all_items(self):
        if self.state != CartState.ACTIVE:
            raise OperationNotAllowedError("Cannot remove items in this state")

        self.items.clear()

        self.state = CartState.EMPTY

    def start_checkout(self):
        if self.state != CartState.ACTIVE:
            raise OperationNotAllowedError("State is not active")

        self.state = CartState.CHECKOUT

    def confirm_order(self):
        if self.state != CartState.CHECKOUT:
            raise OperationNotAllowedError("State is not checkout")

        self.state = CartState.ORDERED





