def invert_numbers(numbers):
    result = []
    for num in numbers:
        try:
            result.append(1 / num)
        except ZeroDivisionError:
            result.append(float("inf"))
    return result


numbers = [1, 2, 0, 3, 4]
print(invert_numbers(numbers))
# [1.0, 0.5, inf, 0.3333333333333333, 0.25]
