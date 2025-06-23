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


if "oolong" in chai_types:
    print("oolong is in the chai_types")
    print(chai_types)
    chai_types["green"]= "fresh"
    print(chai_types)
    chai_types["masala"]="spicy"
    print(chai_typess)
    
    
    
    if "oolong"in chai_types:
        print("oolong in chai_types")