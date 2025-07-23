# def is_prime(n):
#     return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# # Example usage:z


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#         else:
#             return True
    

# # Example usage:
# number = 4
# print(is_prime(number))


def is_prime(n):
    return n>1 and all(n%i !=0 for i in range(2,int(n**0.5+1)))

number = 65
print(is_prime(number))







n=36

for i in range(1,n+1):
    if n%i == 0:
        print(i)
            
def print_divisors(n):
    print(f"Divisors of {n} are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

# Example usage
number = 65

print_divisors(number)


            
            
            