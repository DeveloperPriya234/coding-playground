chai_types ={"masala":"spicy","ginger":"zesty","green":"fresh"}

print(chai_types)

print(chai_types["masala"])


chai_types["masala"] = "very spicy"
print(chai_types)

chai_types["oolong"] = "smooth"
print(chai_types)


print(chai_types.get("masala"))
chai_types.pop("ginger")
print(chai_types)

print(chai_types.popitem())