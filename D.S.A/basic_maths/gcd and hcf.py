# import math

# def find_hcf(a, b):
#     return math.gcd(a, b)

# # Example
# num1 = 36
# num2 = 60
# print("HCF is:", find_hcf(num1, num2))



# def find_hcf(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# # Example
# num1 = 36
# num2 = 60
# print("HCF is:", find_hcf(num1, num2))









# def find_hcf(a, b):
#     hcf = 1
#     for i in range(1, min(a, b) + 1):
#         if a % i == 0 and b % i == 0:
#             hcf = i
#     return hcf

# # Example
# num1 = 36
# num2 = 60
# print("HCF is:", find_hcf(num1, num2))


def find_gcd(a,b):
    hcf = 1
    for i in range(1,min(a,b)+1):
        if a % i == 0 and b%i == 0:
            gcd = i
    return gcd
num1 = 3
num2 = 9
print("gcd is:",find_gcd(num1,num2))
            
    