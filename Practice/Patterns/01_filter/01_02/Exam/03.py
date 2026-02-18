movies = [
    {"title": "Interstellar", "rating": 8.6, "year": 2014},
    {"title": "Avatar",       "rating": 7.8, "year": 2009},
    {"title": "Dune",         "rating": 8.1, "year": 2021},
    {"title": "The Room",     "rating": 3.7, "year": 2003},
    {"title": "Tenet",        "rating": 7.3, "year": 2020},
    {"title": "Arrival",      "rating": 7.9, "year": 2016},
]

filtered = []
for movie in movies:
    if movie["rating"] >= 8.0 and movie["year"] > 2010:
        filtered.append(movie)

result = []
for movie in filtered:
    result.append({
        "movie": movie["title"].upper(),
        "score": movie["rating"] * 10,
        "age": 2025 - movie["year"]
    })

print("Result:", result)