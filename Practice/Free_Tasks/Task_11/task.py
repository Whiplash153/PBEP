num = [5, 4, 5, 3, 4]

def average_mark(data):
        if not data:
            return None
        else:
            total = 0
            for mark in data:
                total += mark
            return total / len(data)

result = average_mark(num)
print("Result:", result)

