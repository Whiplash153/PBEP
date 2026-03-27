class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi! I'm {self.name}, {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def study(self):
        print(f"{self.name} studies {self.major}.")