def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(7)

def factorial(n):
    if(n==0 or n==1):
        return 1
    print(n)
    return (n*factorial(n-1))
print((factorial(7)))
    
    
    