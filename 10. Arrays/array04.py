n = int(input("n = "))
a = int(input("a = "))
d = int(input("d = "))
ar = []
for i in range(n):
    ar.append(a * d**i)
print(ar)