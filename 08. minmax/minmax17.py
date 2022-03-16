n = int(input("n = "))
x = True
i = 1

while n >= i:
    a = int(input("a = "))
    if x:
        maxi = a
        k = i
        x = False
    if maxi <= a:
        maxi = a
        k = i
    i += 1
print(n - k)
