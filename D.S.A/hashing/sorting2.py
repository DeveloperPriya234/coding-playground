#bubble sort
numbers = [5, 2, 9, 1, 7]

for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Descending:", numbers)
