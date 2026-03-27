class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"Woof! My name is {self.name}")

    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! Now you are {self.age}.")

p = Dog("Rex", 8)
p.bark()
p.birthday()
