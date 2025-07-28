#print from 1 to n(dont allow to use (i+1,n)

def print_numbers(Lrange,Urange):
    if Lrange < Urange:
        return
    else:
        
        print(Lrange)
        print_numbers(Lrange-1,Urange)
print(print_numbers(10,1))
    