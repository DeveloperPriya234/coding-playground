# given an integer check if it is prime or not prime true if number is prime .print false


num = 55
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
``
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")
