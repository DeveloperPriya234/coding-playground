
def recursive_string(s):
    if len(s) == 0:
        return ""
    else:
        return recursive_string(s[1:]) + s[0]
print(recursive_string("1,2,3,4,5"))
