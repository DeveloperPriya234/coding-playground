def print_numbers(Lrange,Urange):
    #base case
    if Lrange > Urange:
        return
    print(Lrange)
    print_numbers(Lrange+1,Urange)
    
print_numbers(1,10)