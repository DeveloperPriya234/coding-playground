#generate function with yield:
# problem:while a generator function the yields even numbers up to a specified limit.

def even_generator(limit):
    list=[]

    for i in  range(2,limit+1,2):
        
        list.append(i)
    return list
      
print(even_generator(10))
      
      
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
        
        
for num in even_generator(10):
    print(num)