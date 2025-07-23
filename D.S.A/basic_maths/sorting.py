def print_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    divisors.sort()  # This ensures they're in ascending order
    print(f"Divisors of {n} are:")
    for d in divisors:
        print(d)

# Example usage
number = 65
print_divisors(number)
