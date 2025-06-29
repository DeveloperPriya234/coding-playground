#function returning multiply values:
# problem: create a function the returns both the area and circumference of a circle given it rdius.

def circm_ar(r):
    pi = 3.14
    area = pi*(r**2)
    circumfrence = 2*pi*r
    return [area,circumfrence]

print(circm_ar(4))

import math
def circle_stats(radius):
    area = math.pi*radius
    circumfrence = 2*math.pi*radius
    return area,circumfrence

a,c = circle_stats(4)
print("area =,",a,"circumfrence =",c,)