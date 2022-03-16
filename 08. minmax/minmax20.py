n = int(input("n = "))
x = True
i = 1
while n >= i:
    a = int(input("a = "))
    if x:
        maxi = a
        mini = a
        k,l = 1,1
        x = False
    else:
        if maxi == mini:
            k = 0
        elif maxi < a:
            maxi = a
            k = 1
        elif maxi == a and maxi != mini:
            k += 1

        if mini > a:
            mini = a
            l = 1
        elif mini == a:
            l += 1
    i += 1
print(k+l)