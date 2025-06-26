#seearch for a number of the following list using loop:

nums = (1,4,9,25,36,49,64,81,100)
x = 36
i = 0
while i < len(nums):
    if(nums[i]==x):
        print("found at index",i)
    i += 1
    
    