def reverse(s):
    res = ""
    for i in s:
        res = i + res
    return res


s = "python is good language"

print(reverse(s))
