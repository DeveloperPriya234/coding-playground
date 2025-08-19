# Generate numbers from 1 to 100
numbers = list(range(1, 101))

# Print the numbers
print("Numbers from 1 to 100:")
print(numbers)

# Calculate the difference between consecutive elements
differences = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]

# Print the differences
print("\nDifferences between consecutive elements:")
print(differences)
