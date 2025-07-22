def pattern12(N):
    # Initial number of spaces
    spaces = 2 * (N - 1)

    # Outer loop for rows
    for i in range(1, N + 1):
        # Print ascending numbers
        for j in range(1, i + 1):
            print(j, end='')

        # Print spaces
        print(' ' * spaces, end='')

        # Print descending numbers
        for j in range(i, 0, -1):
            print(j, end='')

        # Move to next line
        print()

        # Decrease space by 2 after each row
        spaces -= 2

def main():
    N = 5  # Change this or use input() to take user input
    pattern12(N)

if __name__ == "__main__":
    main()
