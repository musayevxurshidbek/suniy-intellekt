n = int(input("n = "))
a = int(input("a = "))
b = int(input("b = "))
mi = a * b
for i in range(1,n):
    a = int(input("a = "))
    b = int(input("b = "))
    if mi > a*b:
        mi = a * b
print(mi)