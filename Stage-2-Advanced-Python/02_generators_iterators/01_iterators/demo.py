from countdown import Countdown

cd = Countdown(5)

for num in cd:
    print(num)

print("Ручная проверка:")
cd2 = Countdown(3)
print(next(cd2))
print(next(cd2))
print(next(cd2))