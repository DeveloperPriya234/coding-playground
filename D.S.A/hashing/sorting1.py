#BUBBLE SORT(ASCENDING ORDER)


numbers = [5, 2, 9, 1, 7]

# Bubble sort using iteration
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            # Swap elements
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)
