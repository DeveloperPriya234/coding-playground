# Create an array (list)
fruits = ["apple", "banana", "cherry"]

# Access elements
print(fruits[0])  # Output: apple

# Modify elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Add elements
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Remove elements
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blueberry', 'orange']

# Loop through array
for fruit in fruits:
    print(fruit)


