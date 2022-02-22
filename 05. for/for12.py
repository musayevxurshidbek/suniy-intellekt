n = int(input("n = "))
s = 1
for i in range(1, n + 1):
    s *= (1 + i/10)
print(s)