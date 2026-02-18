from account import Account

acc = Account("Misha", 0)

acc.withdraw(50)
acc.deposit(200)
acc.withdraw(150)
print("Balance:", acc.get_balance())
