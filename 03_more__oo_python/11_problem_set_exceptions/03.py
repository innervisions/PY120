try:
    first = float(input("Please enter the first number: "))
    second = float(input("Please enter the second number: "))
    result = first / second
except (ValueError, ZeroDivisionError) as e:
    print(e)
else:
    print(f"{first} / {second} = {result}")
finally:
    print("End of the program")
