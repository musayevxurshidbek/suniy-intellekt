n = int(input("n = "))
x = float(input("x = "))
s = 0
t = 1
for i in range(1,n+1):
    s += t * x**(2*i+1)/(2*i+1)
    t *= -1
print(s)