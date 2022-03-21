def Triangle(x):
    from math import sin, pi
    return 3 * x, x * x * sin(pi / 3)


a = float(input("a = "))
b = float(input("a = "))
c = float(input("a = "))
print(Triangle(a))
print(Triangle(b))
print(Triangle(c))
