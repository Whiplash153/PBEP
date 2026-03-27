class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} deposited to {self.owner}'s account. Balance: {self._balance}")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn from {self.owner}'s account. Balance: {self._balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self._balance


