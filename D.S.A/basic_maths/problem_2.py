# #problem2:
# #write program to generate the reverse of a given number N. PRINT THE CORRESPONDING REVERSE NUMBER .
# #NOTE:
#  if a number has trolling zeroes then its reverse wil not iclude them for eg reverse of 10400 wil be 401 istead of 00401# Program to reverse a given number N

# Take input from user
N = 1223

# Reverse the number using string slicing and remove leading zeros by converting back to int
reversed_number = int(str(N)[::-1])

# Print the result
print("Reversed number:", reversed_number)
