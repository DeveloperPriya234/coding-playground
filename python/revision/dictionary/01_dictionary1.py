chai_types = {"masala":"spicy","ginger":"zesty","green":"mild"}

print (chai_types["masala"])

(chai_types["green"]) = "fresh"

print(chai_types)

for chai in chai_types:
    print(chai, chai_types[chai])
    
    print(chai_types.get("masala"))

chai_types["ginger"] = "zesty"
print(chai_types)


for chai in chai_types:
    print(chai)
for chai in chai_types:
    print(chai,chai_types[chai])


for key,value in chai_types.items():
    print(key,value-)