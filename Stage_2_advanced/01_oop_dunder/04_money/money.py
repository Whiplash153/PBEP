class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

    def __repr__(self):
        return f"Money(amount={self.amount}, currency='{self.currency}')"

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            raise ValueError("Different currencies")
        return Money(self.amount - other.amount, self.currency)

    def __eq__(self, other):
        if self.currency != other.currency:
            raise ValueError("Different currencies")
        return self.amount == other.amount