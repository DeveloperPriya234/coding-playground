chai_types = {"masala":"spicy","ginger":"zesty","green":"fresh"}

chai_types["earl grey"]=  "citrus"
print(chai_types)

chai_types.pop("ginger")
print(chai_types)

chai_types["ginger"]= "zesty"
print(chai_types)

print(chai_types.pop("ginger"))
print(chai_types)

(chai_types.popitem())
print(chai_types)

chai_types["oolong"]= "smooth"
print(chai_types)
chai_types["ginger"]="zesty"

print(chai_types)

chai_types.popitem()
print(chai_types)
print(len(chai_types))

chai_types = chai_types.copy()
print(chai_types)
print(chai_types.copy())
print(chai_types is chai_types.copy())
print(chai_types == chai_types.copy())