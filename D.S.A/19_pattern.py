def pattern19(N):
    # Upper half
    iniS = 0
    for i in range(N):
        # Left stars
        print('*' * (N - i), end='')
        # Middle spaces
        print(' ' * iniS, end='')
        # Right stars
        print('*' * (N - i))
        # Increase middle spaces
        iniS += 2

    # Lower half
    iniS = 2 * N - 2
    for i in range(1, N + 1):
        # Left stars
        print('*' * i, end='')
        # Middle spaces
        print(' ' * iniS, end='')
        # Right stars
        print('*' * i)
        # Decrease middle spaces
        iniS -= 2

# Example usage
N = 5
pattern19(N)
