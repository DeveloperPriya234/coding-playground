def erect_pyramid(N):
    # Outer loop for the number of rows
    for i in range(N):
        # Print spaces before the stars
        print(' ' * (N - i - 1), end='')
        # Print stars
        print('*' * (2 * i + 1), end='')
        # Print spaces after the stars (optional for symmetry)
        print(' ' * (N - i - 1), end='')
        # Move to the next line
        print()

def inverted_pyramid(N):
    # Outer loop for the number of rows
    for i in range(N):
        # Print spaces before the stars
        print(' ' * i, end='')
        # Print stars
        print('*' * (2 * N - (2 * i + 1)), end='')
        # Print spaces after the stars (optional for symmetry)
        print(' ' * i, end='')
        # Move to the next line
        print()
def main():
    N = 5  # You can change this or take input from the user
    erect_pyramid(N)
    inverted_pyramid(N)

if __name__ == "__main__":
    main()
