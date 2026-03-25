from money import Money

usd1 = Money(50, "USD")
usd2 = Money(25.75, "USD")
eur1 = Money(10, "EUR")

print(usd1)
print(usd2)

total = usd1 + usd2
print(total)

diff = usd1 - usd2
print(diff)

print(usd1 == usd2)
print(usd1 == Money(50, "USD"))

try:
    wrong = usd1 + eur1
except ValueError as e:
    print("Error:", e)