class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.name}! Now you are {self.age}.")

