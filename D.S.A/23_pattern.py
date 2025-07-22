def pattern22(n):
    # Outer loop for rows
    for i in range(2 * n - 1):
        # Inner loop for columns
        for j in range(2 * n - 1):
            # Compute distance from top, bottom, left, and right
            top = i
            left = j
            bottom = (2 * n - 2) - i
            right = (2 * n - 2) - j

            # Compute the minimum distance to an edge and subtract from n
            print(n - min(min(top, bottom), min(left, right)), end=" ")
        print()  # Newline after each row

# Example usage
N = 5
pattern22(N)
