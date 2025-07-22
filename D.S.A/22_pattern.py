def pattern21(n):
    # Outer loop for number of rows
    for i in range(n):
        # Inner loop for number of columns
        for j in range(n):
            # Print '*' if it's a border position
            if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        # Move to the next line after each row
        print()

# Example usage
N = 5
pattern21(N)
