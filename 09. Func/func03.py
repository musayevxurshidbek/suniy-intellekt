def mean(x, y):
    from math import sqrt
    if x * y >= 0:
        return (x + y) / 2, sqrt(x * y)
    else:
        return (x + y) / 2, "O'rta geometrik mavjud emas"


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
print(mean(a, b))
print(mean(a, c))
print(mean(a, d))
