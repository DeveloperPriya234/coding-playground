
#!recursion
#!when a function calls itself repeatly:
 #!prints n to 1 backwards
 
#? def show(n):
#!?    if(n==0):
# ?       return
# * print(n)
# *show(n-1)
#*recursive

# def show(n):
#     if(n==0):#base case
#         return
#     print(n)
#     show(n-1)
    
# show(5)

# 5 * 4 * 3 * 2 * 1 = 

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Example usage
print(factorial_recursive(5))  # Output: 120


def factorial_with_steps(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        print(f"{n}! = 1")
        return 1
    else:
        factors = [str(i) for i in range(n, 0, -1)]
        expression = " * ".join(factors)
        result = 1
        for i in range(n, 0, -1):
            result *= i
        print(f"{expression} = {result}")
        return result

# Example usage
factorial_with_steps(5)
