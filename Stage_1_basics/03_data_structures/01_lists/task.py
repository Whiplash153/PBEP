def f_and_last(seq):
    if not seq:
        return None
    return(seq[0], seq[-1])

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(f_and_last(data))