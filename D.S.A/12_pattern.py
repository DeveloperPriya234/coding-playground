def pattern11(N):
    # First row starts with 1
    for i in range(N):
        # Start with 1 if row is even, 0 if odd
        start = 1 if i % 2 == 0 else 0

        for j in range(i + 1):
            print(start, end='')
            start = 1 - start  # Toggle between 1 and 0

        # Move to next line after each row
        print()

def main():
    N = 5  # You can change this or use input() to get user input
    pattern11(N)

if __name__ == "__main__":
    main()
