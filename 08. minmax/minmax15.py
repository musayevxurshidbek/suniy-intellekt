b = int(input("b = "))
c = int(input("c = "))
n = int(input("n = "))
x = True
i = 1
while n >= i:
    a = int(input("a = "))
    if x and a>=b and a<=c:
        maxi = a
        x = False
    if a>=b and a<=c and maxi < a:
        maxi = a
    i += 1
print(maxi)