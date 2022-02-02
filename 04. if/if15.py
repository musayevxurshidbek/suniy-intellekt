a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
ab = a + b
ac = a + c
bc = b + c
if ab > ac and ab > bc:
    print(a,b)
elif ac > ab and ac > bc:
    print(a,c)
else:
    print(b,c)