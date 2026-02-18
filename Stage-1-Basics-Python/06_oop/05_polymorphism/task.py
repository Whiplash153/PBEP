class Animal:
    def sound(self):
        raise NotImplementedError

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

for p in [Dog(), Cat()]:
    print(p.sound())
