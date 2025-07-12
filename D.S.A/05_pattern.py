def pattern5(N):
    # Outer loop for rows
    for i in range(N):
        # Inner loop prints decreasing number of stars
        for j in range(N, i, -1):
            print("*", end=" ")
        print()  # Newline after each row

# Main block
if __name__ == "__main__":
    N = 5  # You can also use: int(input("Enter N: "))
    pattern5(N)
