def is_valid_palindrome(s: str) -> bool:
    # Filter out non-alphanumeric characters and convert to lowercase
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    # Compare the string with its reverse
    return filtered == filtered[::-1]

# Example usage
print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_valid_palindrome("race a car"))                      # False
print(is_valid_palindrome("No 'x' in Nixon"))                 # True

