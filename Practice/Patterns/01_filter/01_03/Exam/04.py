movies = [
    {"title": "Interstellar", "meta": {"year": 2014, "length": 169}, "ratings": [9.0, 9.5, 8.8]},
    {"title": "Avatar",       "meta": {"year": 2009, "length": 162}, "ratings": [7.8, 8.0, 7.5]},
    {"title": "Dune",         "meta": {"year": 2021, "length": 155}, "ratings": [8.1, 8.4, 8.7]},
    {"title": "The Room",     "meta": {"year": 2003, "length": 99},  "ratings": [3.0, 2.8, 3.5]},
    {"title": "Tenet",        "meta": {"year": 2020, "length": 150}, "ratings": [7.5, 7.8, 7.9]},
]

filtered = []
for movie in movies:

    year_ok = movie["meta"]["year"] >= 2010
    length_ok = movie["meta"]["length"] >= 150
    avg_ok = sum(movie["ratings"]) / len(movie["ratings"]) >= 8.0

    if year_ok and length_ok and avg_ok:
        filtered.append(movie)

result = []
for movie in filtered:
    avg_score = sum(movie["ratings"]) / len(movie["ratings"])

    if avg_score >= 9:
        category = "MASTERPIECE"
    elif avg_score >= 8.5:
        category = "GREAT"
    else:
        category = "GOOD"

    result.append({
        "movie": movie["title"].upper(),
        "avg_score": round(avg_score),
        "category": category
    })

print(result)