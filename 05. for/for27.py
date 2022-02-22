n = int(input("n = "))
x = float(input("x = "))
p1 = 1
p2 = 2
s = 0
for i in range(1, n + 1):
    s += p1 * x ** (2 * i + 1) / (p2 * (2 * i + 1))
    p1 *= (2 * i - 1)
    p1 *= 2 * (i + 1)
print(s)
