#print n to 1

def print_numbers(Lrange,Urange):
    if Lrange > Urange:
        return
    print_numbers(Lrange+1,Urange)
    print(Lrange)
print(print_numbers(1,10))