n = int(input("n = "))
x = float(input("x = "))
s = 0
p = x
for i in range(1,n+1):
    s += p / i
    p *= -x
print(s)