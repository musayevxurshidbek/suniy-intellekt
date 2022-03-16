n = int(input("n = "))
x = True
i = 1
while n >= i:
    a = int(input("a = "))
    if x:
        maxi = a
        mini = a
        k,l = i,i
        x = False
    if maxi < a:
        maxi = a
        k = i
    if mini > a:
        mini = a
        l = i
    i+=1
if k < l:
    print(k)
else:
    print(l)