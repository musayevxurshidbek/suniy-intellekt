p = int(input('p = '))
s = 10
k = 0
while s < 200:
    s *= (1 + p/100)
    k += 1
print("s =",s,"kun =",k)