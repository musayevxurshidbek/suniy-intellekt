a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
a = a + b + c
c = a - (b + c)
b = a - (b + c)
a = a - (b + c)

print(a,b,c)
