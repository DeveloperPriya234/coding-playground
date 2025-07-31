# prestoring valies into same dataastructure like list/dictionary/sets and the fetting


n = [5,3,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]


for num in m :
    i = 0
    for x in n :
        if x == num:
            i+= 1
    print(i)
    