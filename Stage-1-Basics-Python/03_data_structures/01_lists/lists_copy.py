def assign_copy_demo():
    a = [1, 2, 3]
    b = a
    b.append(4)
    return a, b

def slice_copy_demo():
    a = [1, 2, 3]
    b = a[:]
    b.append(4)
    return a, b

def list_copy_method():
    a = [1, 2, 3]
    b = a.copy()
    b.append(4)
    return a, b

def copy_module_demo():
    import copy
    a = [[1, 2], [3, 4]]
    b = copy.deepcopy(a)
    b[0].append(99)
    return a, b

if __name__ == "__main__":
    print("assign_copy_demo:", assign_copy_demo())
    print("slice_copy_demo:", slice_copy_demo())
    print("list_copy_method:", list_copy_method())
    print("copy_module_demo:", copy_module_demo())
