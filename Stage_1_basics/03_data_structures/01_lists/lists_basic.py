empty = []
numbers = [1, 2, 3, 4, 5]
words = ["python", "java", "c++"]
mixed = [10, "hello", True, 3.14]

len_numbers = len(numbers)

first = numbers[0]
last = numbers[-1]

mid = numbers[1:4]
head = numbers[:3]
tail = numbers[2:]
step2 = numbers[::2]

numbers_copy = numbers[:]

def first_and_last(seq):
    if not seq:
        return None
    return (seq[0], seq[-1])

def middle_slice(seq):
    if len(seq) < 3:
        return []
    return seq[1:-1]