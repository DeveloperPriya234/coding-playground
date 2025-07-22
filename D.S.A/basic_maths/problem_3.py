#palindrome number:
#problem3:
#write a program to determine if given number is polindrome or not.print true if it is polindrome.false  otherwise 


#polindrome. are the number for which reverse is exactly same as the original one for eg.121# Function to check if a number is palindrome
def is_palindrome(number):
    original = str(number)
    reversed_number = original[::-1]
    return original == reversed_number

# Example usage:
num = 0000
print(is_palindrome(num))
