class Payment:
    def pay(self, amount):
        raise NotImplementedError

class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} with card."

class CashPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} in cash."

for p in [CardPayment(), CashPayment()]:
    def pay(self, amount):
        return f"Paid {amount} in cash."
    print(p.pay(100))

