def pattern20(n):
    # Initialize the spaces
    spaces = 2 * n - 2

    # Outer loop for rows
    for i in range(1, 2 * n):
        # Determine number of stars
        stars = i if i <= n else 2 * n - i

        # Print left stars
        print("*" * stars, end="")

        # Print spaces
        print(" " * spaces, end="")

        # Print right stars
        print("*" * stars)

        # Update space count
        if i < n:
            spaces -= 2
        else:
            spaces += 2

# Example usage
N = 5
pattern20(N)
