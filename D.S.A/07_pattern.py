def pattern7(N):
    for i in range(N):
        # Print spaces before stars
        for j in range(N - i - 1):
            print(" ", end="")

        # Print stars
        for j in range(2 * i + 1):
            print("*", end="")

        # Print spaces after stars (optional, same as before)
        for j in range(N - i - 1):
            print(" ", end="")

        # Move to the next line
        print()

# Main block
if __name__ == "__main__":
    N = 5  # You can change this or use: int(input("Enter N: "))
    pattern7(N)
