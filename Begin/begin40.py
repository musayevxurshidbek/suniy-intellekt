a1 = float(input("A1 = "))
b1 = float(input("B1 = "))
c1 = float(input("C1 = "))
a2 = float(input("A2 = "))
b2 = float(input("B2 = "))
c2 = float(input("C2 = "))

d = a1 * b2 - a2 * b1
x = (c1 * b2 - c2 * b1) / d
y = (a1 * c2 - a2 * c1) / d
print(x,y)