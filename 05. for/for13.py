n = int(input("n = "))
s = 0
t = 1
for i in range(1,n+1):
    s += t * (1 + i/10)
    t = -t
print(s)