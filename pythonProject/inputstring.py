def inputstring(s):
    f = 0
    for i in s:
        f += 1
    return f


s = input("Enter a string: ")
if inputstring(s) < 1:
    print("enter A string")
elif inputstring(s) % 2 == 0:
    print("You have entered correct string")
elif inputstring(s) % 2 != 0:
    print("you have entered wrong string")
