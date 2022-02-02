x = int(input("x = "))
y = int(input("y = "))
if x * y > 0:
    if x > 0:
        print("I")
    else:
        print("III")
else:
    if x > 0:
        print("IV")
    else:
        print("II")