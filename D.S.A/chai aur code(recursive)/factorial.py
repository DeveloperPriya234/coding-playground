def find_factorial(n):
    result = 1
    for i in range (2,n+1):
        result *= i
    return result
print(find_factorial(8))

def factorial_recursive(n):
    if n ==0 or n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
print(factorial_recursive(4))