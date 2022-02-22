n = int(input("n = "))
a = float(input("a = "))
s = 1
for i in range(1,n + 1):
    s *= a
    print(s)