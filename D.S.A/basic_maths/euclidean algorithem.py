#equilateral algorithm
#gcd(a,b)= gcd(a-b,b) if a >bdef gcd_subtraction(a, b):
def gcd_subtraction(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a  # ya b, dono equal honge

# Example:
print("GCD of 35 and 25 is:", gcd_subtraction(35, 25))

def gcd_find(a,b):
    if a == b:
        return a
    elif a>b:
        return gcd_find(a-b,b)

    else:
        return gcd_find(a,b-a)

    


print("gcd of 35 and 25 is:",gcd_find(35,25))

