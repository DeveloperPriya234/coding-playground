#lambda function:
# problem: create a lambda unction to compute the cube of a number.

# def cube(a,b):
#     return a+b

# result = cube(1,3)


def cube(num):
    return num ** 3
print(cube(2))


cube = lambda x: x**3
print(cube(3))

