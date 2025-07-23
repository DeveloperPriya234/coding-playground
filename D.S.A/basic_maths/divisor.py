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
            