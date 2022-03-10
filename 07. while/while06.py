n = int(input("n = "))
fak = 1
while n > 1:
    fak *= n
    n -= 2

print(fak)