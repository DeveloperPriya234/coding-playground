def pattern15(N):
    # Outer loop for rows
    for i in range(N):
        # Inner loop for characters from 'A' to 'A' + (N - i - 1)
        for ch in range(ord('A'), ord('A') + (N - i)):
            print(chr(ch), end=' ')
        print()  # Move to the next line

# Example usage
N = 5
pattern15(N)
