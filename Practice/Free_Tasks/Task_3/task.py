orders = [
    "Сургут, ул. Ленина, 10",
    "Москва, ул. Тверская, 5",
    "Сургут, ул. Ленина, 10",
    "Тюмень, ул. Республики, 45",
    "Москва, ул. Арбат, 3",
    "Москва, ул. Тверская, 5"
]

unique_orders = set(orders)

print(unique_orders)
print(len(unique_orders))

print("Уникальные адреса доставки:")
for address in unique_orders:
    print("-", address)
print("Всего уникальных адресов:", len(unique_orders))