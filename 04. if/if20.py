a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if abs(a - b) < abs(a - c):
    print("b nuqta", abs(a - b))
else:
    print("c nuqta", abs(a - c))