def contains(seq, value):
    return value in seq

def first_index(seq, value):
    try:
        return seq.index(value)
    except ValueError:
        return None

def count_occurrences(seq, value):
    return seq.count(value)

def numbers_stats(nums):
    if not nums:
        return None
    total = sum(nums)
    return {
        "min": min(nums),
        "max": max(nums),
        "sum": total,
        "avg": total / len(nums),
    }

def reverse_in_place(lst):
    lst.reverse()
    return lst

def sorted_copy(nums, reverse=False):
    return sorted(nums, reverse=reverse)

def top_n(nums, n):
    if n <= 0 or not nums:
        return []
    return sorted(nums, reverse=True)[:n]

if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print(contains(data, 5))
    print(first_index(data, 9))
    print(count_occurrences(data, 5))
    print(numbers_stats(data))
    print(reverse_in_place(data[:]))
    print(sorted(data))
    print(sorted_copy(data, reverse=True))
    print(top_n(data, 3))

