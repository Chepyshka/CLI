def f(n):
    sorted_n = sorted(n, reverse=True)
    return sorted_n[:5]

# Основний код
numbers = {3, 7, 2, 9, 5, 1, 8, 6, 4}
result = f(numbers)
print(result)
