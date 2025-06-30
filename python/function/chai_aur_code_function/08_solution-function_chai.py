#function with **kwargs:
# problem:create a function that accepts any number of keyword arguments and prints them in the format key:value

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    
print_kwargs(name = "priya",age=18,education=12,location="noida")


def print_kwargs(**kwargs):
    for key ,value in kwargs.items():
        print(f"{key}:{value}")
        print(type(kwargs))
        
print_kwargs(name="shaktiman")
