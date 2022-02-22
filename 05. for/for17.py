n = int(input("n = "))
a = float(input("a = "))
s = 1
p = 1
for i in range(1,n + 1):
    p *= a
    s += p
print(s)