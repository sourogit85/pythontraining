def whitespace(s):
    f = 0

    # loop for search each index
    for i in s:

        if i == " ":
            f += 1

    return f


s = "python is good language"
a = s.count(" ")
print(whitespace(s))
print(a)
