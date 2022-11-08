def logic(s):
    for i in s:
        a = ord(i)
        if(a%2==0):
            print("even")
        else:
            print("odd")
    return i
s=input("enter a char:")
print(logic(s))