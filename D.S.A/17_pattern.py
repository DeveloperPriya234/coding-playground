def pattern16(N):
    # Outer loop for rows
    for i in range(N):
        # Determine the character for the current row
        ch = chr(ord('A') + i)
        # Print the character i + 1 times
        for j in range(i + 1):
            print(ch, end=' ')
        print()  # Newline after each row

# Example usage
N = 5
pattern16(N)
