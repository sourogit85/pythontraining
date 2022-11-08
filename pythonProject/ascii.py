def asci(s):
    sa = 0
    m = 1

    for i in s:
        a = ord(i)
        sa = sa + a
        m = m * a
        print(i, " ", a)
    print("sum:", sa)
    print("multiplication:", m)

    #return s


s = input("Enter a string: ")
print( asci(s))