#count digits in a number:
#problem 1:
# given the number n find out and return the number of digits present in a number

# def count_digits(b):
#     # Convert number to positive and count digits
#     return len(str(abs(b)))

# # Example usage
# b = 2345
# print("Number of digits:", count_digits(b))
import math

def count_digits(b):
    if b == 0:
        return 1  # log10(0) is undefined, but 0 has 1 digit
    return int(math.log10(abs(b))) + 1

# Example usage
b = 5454

print("Number of digits:", count_digits(b))
