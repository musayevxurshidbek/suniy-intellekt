n = int(input("n = "))
ar = [0, 1]
for i in range(2, n):
    ar.append(ar[i - 1] + ar[i - 2])
print(ar)
