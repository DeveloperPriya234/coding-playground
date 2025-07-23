def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

number = 65
print(get_divisors(number))


def is_prime(n):
    if n <= 1:
        return False  # 1 or below are not prime
    for i in range(2, int(n**0.5) + 1):  # Check up to √n
        if n % i == 0:
            return False  # Found a divisor, not prime
    return True  # No divisors found, it's prime
print(is_prime(2))    # True
print(is_prime(15))   # False
print(is_prime(17))   # True
print(is_prime(1))    # False
print(is_prime(97))   #