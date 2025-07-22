def pattern20(n):
    # Initialize the number of spaces
    spaces = 2 * n - 2

    # Loop through 2n - 1 rows
    for i in range(1, 2 * n):
        # Calculate number of stars
        stars = i if i <= n else 2 * n - i

        # Print left stars
        print('*' * stars, end='')

        # Print middle spaces
        print(' ' * spaces, end='')

        # Print right stars
        print('*' * stars)

        # Adjust space count
        if i < n:
            spaces -= 2
        else:
            spaces += 2

# Example usage
N = 5
pattern20(N)
