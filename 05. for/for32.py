n = int(input("n = "))
a0 = 1
for k in range(1, n + 1):
    a0 = (a0 + 1) / k
    print(a0)
