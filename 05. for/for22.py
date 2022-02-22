n = int(input("n = "))
x = float(input("x = "))
s = 1
dar = 1
fakt = 1
for i in range(1, n + 1):
    dar *= x
    fakt *= i
    s += dar/fakt
print(s)
