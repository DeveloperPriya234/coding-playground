def reverse_string(s):
    reverse_string = ""
    for char in s:
        reverse_string = char + reverse_string
        return reverse_string
    
    
    
    

def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str  # prepend each character
    return reversed_str

# Example usage
text = "hello"
result = reverse_string(text)
print(result)
