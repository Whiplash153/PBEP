nums = [1, 2, 3]

nums.append(4)
nums.extend([5, 6])
nums.insert(1, 10)

nums.pop()
nums.pop(2)
nums.remove(10)
del nums[0]
nums.clear()

def clean_and_add(seq, element):
    result = seq[:]
    while None in result:
        result.remove(None)
    result.append(element)
    return result