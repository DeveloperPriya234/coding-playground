# # when a function call itself its called a recursion

def find_factorial(n):
    if n== 0:
        return 1
    else:
        return n * find_factorial(n-1)
print(find_factorial(8))


def factorial_with_steps(n):
    def helper(n):
        if n == 1:
            return "1", 1
        else:
            expr, val = helper(n - 1)
            return f"{n} * {expr}", n * val

    expression, result = helper(n)
    print(f"{expression} = {result}")

# Example usage
factorial_with_steps(5)

n = 5
result = 1

for i in range(n, 0, -1):
    result *= i
    print(i, end=" * " if i != 1 else " = ")

print(result)

``