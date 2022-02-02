a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a < b < c or a>b>c:
    a,b,c = a*2,b*2,c*2
else:
    a,b,c = -a,-b,-c
print(a,b,c)