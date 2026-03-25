from money import Money

rub1 = Money(1000, "RUB")
rub2 = Money(350, "RUB")
usd1 = Money(20, "USD")
usd2 = Money(5, "USD")

total = rub1 + rub2
print(total)

diff = rub1 - rub2
print(diff)

print(usd1 == usd2)

try:
    wrong = rub1 + usd2
except ValueError as e:
    print("Error:", e)
