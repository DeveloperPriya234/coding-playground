def pattern8(N):
    # Outer loop for the number of rows
    for i in range(N):
        # Print leading spaces
        for j in range(i):
            print(" ", end="")

        # Print stars
        for j in range(2 * N - (2 * i + 1)):
            print("*", end="")

        # Print trailing spaces (optional in this pattern)
        for j in range(i):
            print(" ", end="")

        # Move to the next line after each row
        print()

# Example usage:
N = 5
pattern8(N)
