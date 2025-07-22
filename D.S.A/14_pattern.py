def pattern13(N):
    # starting number
    num = 1

    # Outer loop for the number of rows
    for i in range(1, N + 1):
        # Inner loop prints i numbers
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        # Line break after each row
        print()

# Example usage
N = 5
pattern13(N)
