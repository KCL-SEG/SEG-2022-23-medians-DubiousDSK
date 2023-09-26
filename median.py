"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()

if len(numbers) % 2 != 0:
    median = numbers[len(numbers) // 2]
else:
    middle1 = numbers[int(len(numbers) / 2)]
    middle2 = numbers[int((len(numbers) / 2) - 1)]
    median = (middle1 + middle2) / 2

print(f"{median} is the median")