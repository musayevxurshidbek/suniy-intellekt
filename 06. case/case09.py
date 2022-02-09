d = int(input("d = "))
m = int(input("m = "))

d += 1
if m in [1,3,5,7,8,10,12]:
    if d > 31:
        m += 1
        if m > 12:
            m = 1
        d -=31
elif m in [4,6,9,11]:
    if d > 30:
        m += 1
        d -= 30
elif m == 2:
    if d > 28:
        m += 1
        d -=28

print(f"{d}/{m}")