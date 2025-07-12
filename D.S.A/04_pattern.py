def pattern3(N):
    # Outer loop for rows (from 1 to N)
    for i in range(1, N + 1):
        # Inner loop for printing numbers from 1 to i
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # Newline after each row

# Main block
if __name__ == "__main__":
    N = 5  # You can also use: int(input("Enter N: "))
    pattern3(N)
