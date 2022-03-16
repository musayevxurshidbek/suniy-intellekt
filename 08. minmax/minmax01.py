n = int(input("n = "))
a = int(input("a = "))
ma = a
mi = a
for i in range(1,n):
    a = int(input("a = "))
    if ma < a:
        ma = a
    if mi > a:
        mi = a

print(ma,mi)