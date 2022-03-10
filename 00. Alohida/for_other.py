n = int(input("n = "))
for i in range(n):
    for j in range(0-i,n-i):
        print(abs(j),end=" ")
    print()