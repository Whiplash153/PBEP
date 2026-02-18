class Countdown:
    def __init__(self, start):
        self.x = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.x <= 0:
            raise StopIteration
        value = self.x
        self.x -= 1
        return value

cd = Countdown(3)

for num in cd:
    print(num)