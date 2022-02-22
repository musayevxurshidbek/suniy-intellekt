n = int(input("n = "))
a1 = 1
a2 = 2
for i in range(3,n+1):
    an = (a2 + 2 * a1)/3
    print(an,end=",")
    a1 = a2
    a2 = an
