def sum_all(*args):
    print(args)
    for i in args:
        print(i*2)#args = tuple,*args = simple
    return  sum(args)

# print(sum_all(1,2,3,4))
print(sum_all(1,2,3))
print(sum_all(2,3,4))
