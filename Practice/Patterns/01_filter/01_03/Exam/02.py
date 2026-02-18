books = [
    {"title": "Dune",          "info": {"pages": 600, "year": 1965}, "rating": 4.9},
    {"title": "1984",          "info": {"pages": 328, "year": 1949}, "rating": 4.8},
    {"title": "The Hobbit",    "info": {"pages": 310, "year": 1937}, "rating": 4.7},
    {"title": "Foundation",    "info": {"pages": 255, "year": 1951}, "rating": 4.6},
    {"title": "Hyperion",      "info": {"pages": 482, "year": 1989}, "rating": 4.4},
]

filtered = []
for book in books:

    pages_ok = book["info"]["pages"] >= 300
    year_ok = book["info"]["year"] < 1970
    rating_ok = book["rating"] >= 4.7

    if pages_ok and year_ok and rating_ok:
        filtered.append(book)

result = []
for book in filtered:

    result.append({
        "book": book["title"].upper(),
        "age": 2025 - book["info"]["year"],
        "weight": "HEAVY" if book["info"]["pages"] >= 500 else "LIGHT"
    })

print(result)
