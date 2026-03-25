class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"This is {self.name}, {self.age} years old.")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

a = Animal("Rex", 5)
a.info()

d = Dog("Rex", 5, "Labrador")
d.bark()

