# given an integer check if it is prime or not prime true if number is prime .print false


# Simple prime number check using a for loop

num = 100

if num <= 1:
    print(num, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
