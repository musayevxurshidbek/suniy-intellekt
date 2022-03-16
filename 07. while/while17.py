n = int(input("n = "))
m = int(input("m = "))
b = 0
while n >= m:
    n -= m
    b += 1
print(b, "butun", n, "qoldiq")
