from domain.states import CartState
from domain.errors import OperationNotAllowedError

class CLI:
    def __init__(self, cart, storage):
        self.cart = cart
        self.storage = storage

    def run(self):

        while True:
            print("\n=== MENU ===")
            print("1. Show cart")
            print("2. Add item")
            print("3. Clear cart")
            print("4. Start checkout")
            print("5. Confirm order")
            print("6. Quit")

            choice = input("\nChoose your number: ").strip()

            try:
                if choice == "1":
                    #SHOW CART
                    print("\nCart ID:", self.cart.id)
                    print("Cart state:", self.cart.state.name)

                    if not self.cart.items:
                        print("Cart has no items")
                    else:
                        print("Cart items:", self.cart.items)

                elif choice == "2":
                    #ADD ITEM
                    add_new_item = input("Enter new item: ").strip()
                    if not add_new_item:
                        print("Field is empty. Please try again.")
                        continue

                    self.cart.add_item(add_new_item)
                    self.storage.save(self.cart)
                    print(f"\nItem {add_new_item} successfully added!")

                elif choice == "3":
                    #CLEAN CART
                    self.cart.remove_all_items()
                    self.storage.save(self.cart)
                    print("\nCart is clear!")

                elif choice == "4":
                    #START CHECKOUT
                    self.cart.start_checkout()
                    self.storage.save(self.cart)
                    print("\nCheckout started")

                elif choice == "5":
                    #CONFIRM ORDER
                    self.cart.confirm_order()
                    self.storage.save(self.cart)
                    print("\nOrder confirmed!")

                elif choice == "6":
                    #QUIT
                    print("\nGOOD BYE!")
                    break

                else:
                    print("\nInvalid choice. Please try again")

            except OperationNotAllowedError as e:
                print("\nError:", e)
