nums = {1, 2, 3, 3, 2}

has_two = 2 in nums

nums.add(4)

size = len(nums)

print(nums)
print("has_two:", has_two)
print("size:", size)

nums.discard(3)

nums.remove(2)

removed = nums.pop()

nums.clear()

print("after operations:", nums)
print("removed element:", removed)
