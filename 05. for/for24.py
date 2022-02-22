n = int(input("n = "))
x = float(input("x = "))
s = 0
dar = 1
fakt = 1.0
t = 1
for i in range(0, n + 1):
    s += (t * dar / fakt)
    dar *= x * x
    fakt *= (i + 1) * (i + 2)
    t *= -1
print(s)
