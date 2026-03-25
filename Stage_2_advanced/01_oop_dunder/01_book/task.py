class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = int(year)

    def __str__(self):
        return f"Movie: {self.title}, {self.year}"

    def __repr__(self):
        return f"Movie(title='{self.title}', year={self.year})"

    def __eq__(self, other):
        if isinstance(other, Movie):
            return self.title == other.title and self.year == other.year
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Movie):
            return self.year < other.year
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Movie):
            return self.year > other.year
        return NotImplemented

m1 = Movie("Inception", "2010")
m2 = Movie("Avatar", "2009")
m3 = Movie("Inception", "2010")

print(m1)
print(m2)
print(m3)

print(repr(m1))
print(repr(m2))
print(repr(m3))

print(m1 == m2)
print(m1 == m3)
print(m2 == m3)

print(m1 > m2)
print(m1 > m3)
print(m2 > m3)

print(m1 < m2)
print(m1 < m3)
print(m2 < m3)

