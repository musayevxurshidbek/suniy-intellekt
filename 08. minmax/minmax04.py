n = int(input("n = "))
a = int(input("a = "))
mi = a
k = 1
for i in range(1,n):
    a = int(input("a = "))
    if mi > a:
        mi = a
        k = i + 1
print(k)