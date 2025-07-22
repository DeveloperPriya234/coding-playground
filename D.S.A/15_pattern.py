def pattern14(N):
    # Outer loop for number of rows
    for i in range(N):
        # Inner loop to print characters from 'A' to 'A' + i
        for ch in range(ord('A'), ord('A') + i + 1):
            print(chr(ch), end=' ')
        # Move to the next line after each row
        print()

# Example usage
N = 5
pattern14(N)
