chai_types = {"masala":"spicy","green":"fresh","ginger":"zesty","oolong":"smooth"}
print(chai_types)

chai_types["ooloong"]= "smooth" and "rich"
print(chai_types)

chai_types["black"] = "strong"
print(chai_types)

chai_types.pop("ginger")
print(chai_types)
chai_types.popitem()
print(chai_types)


for chai in chai_types:
    print(chai)
    for chai in chai_types:
        print(chai,chai_types[chai])
        chai_types.items()

for key,value in chai_types.items():
    print(key,value)
    
    
if "masala"in chai_types:
    print("i have masala chai in chai_types")
    
    tea_shop = {"chai":{"masala":"spicy","ginger":"zesty"},"tea":{"green":"fresh","black":"strong"}}
    print(tea_shop)
    print(tea_shop["chai"])
    print(tea_shop["tea"])
    
    
squared_num = {x:x**2 for x in range(10)}
print(squared_num)