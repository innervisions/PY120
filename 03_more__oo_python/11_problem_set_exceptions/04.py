num = float(input("Enter a number: "))
if num < 0:
    raise ValueError("Negative numbers are not allowed!")
print(f"You entered {num}")
