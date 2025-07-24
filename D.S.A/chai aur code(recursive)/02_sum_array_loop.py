# # def sum_iterative(arr):
# #     total = 0
# #     for num in arr:
# #         total += num
# #         return total
# # print(sum_iterative([1,2,3,4,5,67,8,9,10]))


# # def sum_two_numbers(a,b,c):
# #     return a+b+c

# # result = (sum_two_numbers(1,2,3))
# # print("sum  of two numbers:",result)



def sum_numbers(*args):
    return sum(args)

result = sum_numbers(1,2,3,4,5,6,7,78,9,10)
print("sum of the numbers:",result)