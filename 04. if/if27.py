x = float(input("x = "))
if x < 0:
    y = 0
elif x % 2 < 1:
    y = 1
else:
    y = -1
print(y)