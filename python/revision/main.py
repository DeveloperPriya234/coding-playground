#function

x = "awesome"
def myfunc():
    print("python is " + x)
    
myfunc()
    
x = "awesome" 
def myfunc():
    x = "fantastic"
    print("python is" + x)
    
myfunc()

print("python is"+ x)

myfunc()
print("print is"+ x)

#the global keyboard
# if use the global keyboard,the variable belongs to the global scope:

def myfunc():
    global x
    x = "fanatastic"
    
myfunc()
print("python is" + x)


#to change the valuenof a global variable inside a function, refer to the variable by using the global keyboard:


x = "awesome"
def  myfunc():
    global x
    x ="fantastic"
myfunc()
print("python is"+ x)