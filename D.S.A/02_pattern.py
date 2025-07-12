
def pattern1(N):
    for i in range(N):
        # Inner loop for printing columns
        for j in range(N):
            print("*", end=" ")
        # Newline after each row
        print()

# Main function
if __name__ == "__main__":
    N = 4  # You can change this value or take user input
    pattern1(N)
