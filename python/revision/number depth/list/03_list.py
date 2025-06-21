tea_varities = ["black","green","oolong","matcha","herbal"]

print(tea_varities)
for tea in tea_varities:
    print(tea)
    
    for tea in tea_varities:
        print(tea,end="-")    
    print("\n")
    
if "matcha"in tea_varities:
    print("matcha is in the tea_varities")
    tea_varities.append("masala")
    print(tea_varities)
    if"masala" in tea_varities:
        print("masala is in the tea_varities")
tea_varities.pop()
print(tea_varities)
tea_varities.remove("herbal")
print(tea_varities)
tea_varities.insert(2,"chai")
print(tea_varities)
tea_varities.sort()
print(tea_varities)
tea_varities.reverse()
print(tea_varities)
tea_varities.count("matcha")
print(tea_varities.count("matcha"))
len(tea_varities)
print(len(tea_varities))
tea_varities.clear()
print(tea_varities)
tea_varities.index("chai")
print(tea_varities.index("chai"))
print(tea_varities)