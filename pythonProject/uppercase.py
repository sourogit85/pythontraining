def uppercase(s):
    res=""
    for i in s:
        if ord(i) > 96:
            i = ord(i) - 32
            res = res+ chr(i)
        else:
            res=res+i
    return res


s = "python is good language"
print(uppercase(s))
print(s.upper())
