

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
    N = 4  # You can also use: N = int(input("Enter N: "))
    pattern2(N)



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


