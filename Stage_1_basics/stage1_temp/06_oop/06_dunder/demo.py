from str_repr import Person, Student

p = Person("Anna", 25)

s = Student("Alex", 20, "Computer Science")

people = [p, s, Person("John", 30), Student("Kate", 22, "Mathematics")]

for person in people:
    print(person)