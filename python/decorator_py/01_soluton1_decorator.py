#problem1: timing function execution
#problem: write a decorator that measures the time a funnction takes to execute


import time

def timer(func):
    def wrappper(*args,**kwargs):
      start = time.time()
      result=  func(*args,**kwargs)
      end = time.time()
      print(f"{func.__name__}ran in{end-start} time")
      return result
    return wrappper
@timer
def example_function(n):
      time.sleep(n)
example_function(2)