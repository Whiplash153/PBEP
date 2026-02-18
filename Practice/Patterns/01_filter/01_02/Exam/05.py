cars = [
    {"brand": "bmw",   "hp": 300, "year": 2018, "awd": True},
    {"brand": "audi",  "hp": 190, "year": 2014, "awd": False},
    {"brand": "tesla", "hp": 450, "year": 2021, "awd": True},
    {"brand": "ford",  "hp": 120, "year": 2008, "awd": False},
    {"brand": "subaru","hp": 250, "year": 2016, "awd": True},
]

filtered = []
for car in cars:
    if car["hp"] >= 200 and car["year"] >= 2015 and car["awd"]:
        filtered.append(car)

result = []
for car in filtered:
    result.append({
        "model": car["brand"].upper(),
        "power_class": "HIGH" if car["hp"] > 300 else "MEDIUM",
        "age": 2025 - car["year"]
    })

print("Result:", result)
