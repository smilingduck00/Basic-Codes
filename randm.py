import random

array = []
for _ in range(3):
    try:
        number = int(input("Enter a number: "))
        array.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Sort it from min to max
print(sorted(array, reverse=False))

# Sort it from max to min
print(sorted(array, reverse=True))

print("Min: ", min(array))
print("Max: ", max(array))
