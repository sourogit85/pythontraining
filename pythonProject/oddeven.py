def length(s):
    f = 0
    for i in s:
        f += 1
    return f
s="souradipta"
print("even chars")
for i in range(length(s)):
    if i % 2 == 0:
        print(s[i])
print("Odd chars")
for i in range(length(s)):
    if i % 2 != 0:
        print(s[i])