n = int(input("n = "))
k = int(input("k = "))
s = 0
while n >= k:
    s += 1
    n -= k
print(f"{s} - butun, {n} - qoldiq")
