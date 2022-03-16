n = int(input("n = "))
k = 1
S = 1
while S<=n:
    k+=1
    S+=k
print(k-1,S-k)