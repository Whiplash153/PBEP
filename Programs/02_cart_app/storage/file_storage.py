import json
from pathlib import Path

from domain.states import CartState
from domain.cart import Cart

class FileStorage:
    def __init__(self, filepath):
        self._filepath = Path(filepath)

    def load(self):
        if not self._filepath.exists():
            return Cart(id=1)
        else:
            with open(self._filepath, "r", encoding="utf-8") as f:
                raw_data = json.load(f)

                cart_id = raw_data["id"]
                cart = Cart(id=cart_id)

                cart.state = CartState[raw_data["state"]]
                cart.items = raw_data["items"]

                return cart

    def save(self, cart: Cart):
        item = {
            "id": cart.id,
            "state": cart.state.name,
            "items": cart.items
        }

        with open(self._filepath, "w", encoding="utf-8") as f:
            json.dump(item, f)









