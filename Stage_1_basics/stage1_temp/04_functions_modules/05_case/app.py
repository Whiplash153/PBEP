import order_calc

cart = [
    (1000, 1),
    (250, 2),
    (99.9, 3),
]

s = order_calc.subtotal(cart)
print("Subtotal:", s)

after_discount = order_calc.apply_discount(s, 10)
print("After discount:", after_discount)

final = order_calc.add_tax(after_discount, 8)
print("Final total:", final)

final12 = order_calc.final_total(cart, discount_percent=10, tax_percent=8)
print("Final total (one_call):", final12)