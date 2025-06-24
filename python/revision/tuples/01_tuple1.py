#tuple is immutable
tea_types = ("black","green","oolong")
print(tea_types)
print(tea_types[0])
print(tea_types[-1])
print(tea_types[1:3])
print(tea_types[1:])
# tea_types[0] = "white"
# print(tea_types)
len(tea_types)
print(len(tea_types))

more_tea = ("herbal","earl grey",)
all_tea =tea_types +more_tea
print(all_tea)
if "green" in all_tea:
    print(" i have green tea in all_tea")
    for tea in all_tea:
        print(tea,end="_")
        more_tea = ("herbal","earl grey","herbal")
        print( more_tea.count("herbal"))
        
    tea_types = ("Black","Green","Oolong")
    print(tea_types)
    
    (black,green,oolong)=tea_types
    print(black)
    print(green)
    print(oolong)
    type(tea_types)
