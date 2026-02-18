def average_mark(data):
    if not data:
        return None

    total = sum(data)
    avg = round(total / len(data), 2)
    return avg


if __name__ == "__main__":
    marks = [5, 4, 5, 3, 4]
    result = average_mark(marks)

    if result is None:
        print("Нет данных для расчёта.")
    else:
        print(f"Средняя оценка: {result}")