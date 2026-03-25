from account import Account

acc1 = Account("Alice", 100)
acc2 = Account("Bob")

acc1.deposit(50)
acc1.withdraw(30)
print("Balance Alice:", acc1.get_balance())

acc2.deposit(200)
acc2.withdraw(250)
print("Balance Bob:", acc2.get_balance())