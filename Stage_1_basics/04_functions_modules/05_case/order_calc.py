def subtotal(items):
    total = 0
    for price, qty in items:
        total = total + price * qty
    return total

def apply_discount(amount, percent=0):
    return amount * (1 - percent / 100)

def add_tax(amount, tax_percent=0):
    return amount * (1 + tax_percent / 100)

def final_total(items, discount_percent=0, tax_percent=0):
    s = subtotal(items)
    after_discount = apply_discount(s, discount_percent)
    return add_tax(after_discount, tax_percent)

