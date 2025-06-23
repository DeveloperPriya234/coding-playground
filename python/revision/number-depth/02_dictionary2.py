chai_types =  {"masala":"spicy","ginger":"zesty","green":"fresh"}
print(chai_types)

chai_types["green"]= "fresh"
print(chai_types)

print(chai_types["masala"])

print(chai_types.get("masala"))

print(chai_types.get("oolong","not found"))


for chai in chai_types:
    print(chai)
    
for chai in chai_types:
    print(chai,chai_types[chai])
    
for key,value in chai_types.items():
    print(key,value)
    if "masala" in chai_types:
        print(" i have masala in chai_types")
else:
    print(" i dont have masala in chai_types")