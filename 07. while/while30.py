a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
m = 0
n = 0
while a >= c:
    a -= c
    m += 1 
while b >= c:
    b -= c
    n += 1
j = 0
while m > 0:
    j += n 
    m -= 1
print(j)