names = ["bob", "alexander", "mia", "jonathan", "ann", "mike"]

result = []
for n in names:
    if len(n) > 3:
        result.append(n.upper())

print(result)