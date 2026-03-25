def notice(func):
    def wrapper(*args, **kwargs):
        print(f"Attention! {func.__name__} function running...")
        result = func(*args, **kwargs)
        print("Done!")
        return result
    return wrapper

@notice
def achieve(car):
    print(f"Car {car} achieved!")

achieve("Volvo")