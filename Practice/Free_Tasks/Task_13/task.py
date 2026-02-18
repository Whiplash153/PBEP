purchases = {
    "Ivan": [1200, 800, 350],
    "Anna": [200, 450],
    "Oleg": []
}

def get_top_customers(data):
    if not data:
        return None

    top_name = None
    top_sum = 0

    for name, summary in data.items():
        customer_sum = sum(summary)
        if customer_sum > top_sum:
            top_sum = customer_sum
            top_name = name

    return top_name

if __name__ == "__main__":
    print(get_top_customers(purchases))

