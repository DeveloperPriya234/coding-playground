def pattern17(N):
    for i in range(N):
        # Print leading spaces
        print(" " * (N - i - 1), end="")

        ch = ord('A')
        breakpoint = (2 * i + 1) // 2

        # Print palindromic alphabet characters
        for j in range(1, 2 * i + 2):  # 2*i+1 characters
            print(chr(ch), end="")
            if j <= breakpoint:
                ch += 1
            else:
                ch -= 1

        # Print trailing spaces (optional, for symmetry)
        print(" " * (N - i - 1))

# Example usage
N = 5
pattern17(N)
