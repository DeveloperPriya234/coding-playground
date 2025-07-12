

def pattern2(N):
    # Outer loop for rows
    for i in range(N):
        # Inner loop for printing stars in each row
        for j in range(i + 1):
            print("*", end=" ")
        # Move to the next line after each row
        print()

# Main function
if __name__ == "__main__":
    N = 5  # You can also use: N = int(input("Enter N: "))
    pattern2(N)





