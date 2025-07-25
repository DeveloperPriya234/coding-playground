# def sum_iterative(arr):
#     total = 0
#     for num in arr:
#         total += num
#     return total
# print(sum_iterative([1,2,3,4,5,6,7,8,9,10]))




def sum_recursive(arr):
    if arr == []:
        return 0
    else:
        return arr[0]+ sum_recursive(arr[1:])
print(sum_recursive([1,2,3,4,5,]))
    
    
    
def sum_recursive(arr):
    if arr == []:
        return 0
    else:
        return arr[0]+ sum_recursive(arr[1:])
print(sum_recursive([1,2,3,4,5,6,7,8,9,10]))
    