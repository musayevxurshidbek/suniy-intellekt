n = int(input("n = "))
m = int(input("m = "))
v = int(input("v = "))
max_ro = m / v
for i in range(1,n):
    m = int(input("m = "))
    v = int(input("v = "))
    if max_ro < m / v:
        max_ro = m / v
print(max_ro)