password = "secure@234"

if len(password) < 6:
    strenghth = ("weak")
    
elif len(password) <= 10 :
    strength =("medium")
elif len(password) > 10:
    strength = ("strong")
    
    
print("password strength is:",strength)