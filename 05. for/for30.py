from math import sin

n = int(input("n = "))
a = float(input("a = "))
b = float(input("b = "))
h = (b - a) / n
for i in range(1, n + 1):
    print(1 - sin(a + (i - 1) * h))
