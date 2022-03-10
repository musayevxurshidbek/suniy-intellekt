n = int(input("n = "))
for j in range(1, n + 1):
    s = 0
    for i in range(1, j // 2 + 1):
        if j % i == 0:
            s += i
    if j == s:
        print(j, end=" ")
