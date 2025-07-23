# given an integer check if it is prime or not prime true if number is prime .print false


# Simple prime number check using a for loop

def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n == 2:
        return True   # 2 is the only even prime number
    if n % 2 == 0:
        return False  # other even numbers are not prime
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Example usage:
number = 23
print(is_prime(number))