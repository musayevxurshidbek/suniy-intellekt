n = int(input("n = "))
a = int(input("a = "))
b = int(input("b = "))
ma = 2 * (a + b)
for i in range(1,n):
    a = int(input("a = "))
    b = int(input("b = "))
    if ma < 2 * (a + b):
        ma = 2 * (a + b)
print(ma)