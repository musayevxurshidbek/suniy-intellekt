n = int(input("n = "))
f1 = 1
f2 = 1
for i in range(3,n+1):
    fn = f2 + f1
    print(fn,end=",")
    f1 = f2
    f2 = fn
