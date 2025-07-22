# armstrong number000000

# write a function to print all divisors of a number divisor are the  numbers that divide the numner entirely and leaves no remainder


def print_divisors(n):
    print(f"Divisors of {n} are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

# Example usage
number = 12
print_divisors(number)
