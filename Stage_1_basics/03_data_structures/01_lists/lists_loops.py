def print_elements(seq):
    for item in seq:
        print(item)

def print_with_index(seq):
    for index, item in enumerate(seq):
        print(index, item)

def squares(nums):
    result = []
    for n in nums:
        result.append(n * n)
    return result

def squares_comp(nums):
    return [n * n for n in nums]

def filter_even(nums):
    return [n for n in nums if n % 2 == 0]

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    print("print elements:")
    print_elements(data)

    print("print with index:")
    print_with_index(data)

    print("squares:")
    print(squares(data))

    print("squares_comp:")
    print(squares_comp(data))

    print("filter_even:")
    print(filter_even(data))




