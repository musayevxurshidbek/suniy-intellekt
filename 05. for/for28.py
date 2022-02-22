n = int(input("n = "))
x = float(input("x = "))
p1 = 1
p2 = 2
s = 1
for i in range(1, n + 1):
    s += (-1)**(i+1) * p1 * x ** i / p2
    p1 *= (2 * i - 1)
    p1 *= 2 * (i + 1)
print(s)
