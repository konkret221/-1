def to_float(num):
    if isinstance(num, (int, float)):
        return float(num)
    return "Невозможно преобразовать"
print(to_float(3.467))
print(to_float('word'))