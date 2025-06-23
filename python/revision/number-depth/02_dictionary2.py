chai_types =  {"masala":"spicy","ginger":"zesty","green":"fresh"}
print(chai_types)

chai_types["green"]= "fresh"
print(chai_types)

print(chai_types["masala"])

print(chai_types.get("masala"))