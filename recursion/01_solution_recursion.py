
#!write a recursive function to calculate the sum off first n natural numbers.


def sum(n):
    if(n==0):
        return  0
    
    return sum (n-1)+n
    
sum = sum(10)
print(sum)