#basic recursion problems
# print name 5 times
#print from n to 1
#print heer earltt from 1 to n
#9but by bacend react)
#print n to 1
#print from n to 1(beektrouble)
def print_name(name, times):
    if times <= 0:
        return
    print(name)
    print_name(name, times - 1)

# Example usage
n = 5
print_name("priya",  n)
