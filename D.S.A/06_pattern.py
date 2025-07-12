def pattern6(N):
    # Outer loop for rows
    for i in range(N):
        # Inner loop for printing numbers from 1 to N - i
        for j in range(N, i, -1):
            print(N - j + 1, end=" ")
        print()  # Newline after each row

# Main block
if __name__ == "__main__":
    N = 5  # You can also take input from user
    pattern6(N)
