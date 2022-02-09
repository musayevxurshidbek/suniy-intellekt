d = int(input("d = "))
m = int(input("m = "))
y = int(input("y = "))
if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
    kabisa = True
else:
    kabisa = False

d += 1
if m in [1,3,5,7,8,10,12]:
    if d > 31:
        m += 1
        if m > 12:
            m = 1
            y += 1
        d -=31
elif m in [4,6,9,11]:
    if d > 30:
        m += 1
        d -= 30
elif m == 2:
    if d > 28 + kabisa:
        m += 1
        d = 1
print(d, m, y, sep="/")
# if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
#     kabisa = True
# else:
#     kabisa = False
# d -= 1
# if d < 1:
#     if m == 3:
#         m = 2
#         d = 29 if kabisa else 28
#     elif m in [4, 6, 9, 11]:
#         m -= 1
#         d = 31
#     else:
#         m -= 1
#         d = 30
#     if m < 1:
#         d = 31
#         m = 12
#         y -= 1


