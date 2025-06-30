# #function with *args:

# # problem: write a function that takes  varibale number of arguments and return their sum.

def add(*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    print(sum)
    
add(1,2,3,4,5,6,7,8,9)



def my_details(name,age):
    return name,age
    
print(my_details(name="priya",age = 18,))



def my_details(**kwargs):
    # print(Kwargs)
    for key,value in kwargs.items():
        print(key,value)
    
my_details(name = "priya",age = 18,education = 18,location = "noida")

