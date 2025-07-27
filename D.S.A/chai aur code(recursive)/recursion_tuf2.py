# print 1 to n

def print_name(Lrange,Urange):
    if Lrange>Urange:
        return
    else:
        print(Lrange)
        print_name(Lrange+1,Urange)
result =print_name(1,10)
print(result)


