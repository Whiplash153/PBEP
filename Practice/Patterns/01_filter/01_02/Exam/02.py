books = [
    {"title": "Dune",            "pages": 500, "genre": "sci-fi"},
    {"title": "Hamlet",          "pages": 200, "genre": "drama"},
    {"title": "Neuromancer",     "pages": 320, "genre": "sci-fi"},
    {"title": "It",              "pages": 1100, "genre": "horror"},
    {"title": "Foundation",      "pages": 250, "genre": "sci-fi"},
    {"title": "The Shining",     "pages": 450, "genre": "horror"},
]

filtered = []
for book in books:
    if book["genre"] == "sci-fi" and book["pages"] > 300:
        filtered.append(book)

result = []
for book in filtered:
    result.append({
        "name": book["title"].upper(),
        "reading_time(hrs)": book["pages"] / 50
    })

print("Result:", result)