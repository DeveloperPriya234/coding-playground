# given an integer check if it is prime or not prime true if number is prime .print false


def print_divisors(n):
    print(f"Divisors of {n} are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
        if n/i == 1:
            print (n/i)

# Example usage
number = 65

print_divisors(number)
