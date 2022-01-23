from math import sqrt
a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
d = b**2-4*a*c
x1 = (-b+sqrt(d))/(2*a)
x2 = (-b-sqrt(d))/(2*a)
print(x1, x2)
