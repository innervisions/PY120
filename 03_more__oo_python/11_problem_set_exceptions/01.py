try:
    first = float(input("Please enter the first number: "))
    second = float(input("Please enter the second number: "))
    result = first / second
except ValueError:
    print("Please make sure you enter valid numbers.")
except ZeroDivisionError:
    print("Division by zero is undefined.")
else:
    print(f"{first} / {second} = {result}")
