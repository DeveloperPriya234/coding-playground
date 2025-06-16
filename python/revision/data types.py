#text type: string
#numeric value :integer,float,complex
#sequence types:list,tuple,range
#maping type: dict
#set types:set,frozen set
#boolean type:bool
#binary types:bytes,bytesarray,memoryview
#none type: none type6

x = 5
print(type(x))#integer
x = "hello world"
print(type(x))#strings
x = 20.5
print(x,(type(x)))#float
x = 1j
print(type(x))#complex
x =["apple","banana","cherry"]
print(type(x))#list
x = ("apple","banana","cherry")
print(type(x))#tuple
x = range(6)
print(type(x))#range
x = {"name": "john", "age": 30}
print(type(x))#dictionary
x= {"apple","banana","cherry"}
print(type(x))#set#set
x = ({"apple","banana","cherry"})
print(type(x))#frozen set
x =True
print(type(x))#boolean
x = None
print(type(x))#none type