#default paraameter value::
# problem: write a function that greets a user.if no name is provide,it should greet with a default name.

def greet(name = "user"):
    return "hello"+name+"!"

print(greet())