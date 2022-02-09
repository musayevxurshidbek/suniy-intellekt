print("1 - Radius, 2 - Diametr,\n3 - Uzunlik, 4 - Yuza")
a = int(input("Birini kiriting: "))
d = "Radius" if a == 1 else "Diametr" if a == 2 else "Uzunlik" if a == 3 else "Yuza"
x = float(input(f"{d}ni kiriting: "))
pi = 3.14
if a == 1:
    print(f"D = {2 * x}, L = {2 * pi * x}, S = {pi * x * x}")
elif a == 2:
    print(f"R = {x / 2}, L = {pi * x}, S = {pi * x * x / 4}")
elif a == 3:
    x = x / (2 * pi)
    print(f"R = {x}, D = {2 * x}, S = {pi * x * x}")
else:
    x = (x / pi) ** 0.5
    print(f"R = {x}, D = {2 * x}, L = {2 * pi * x}")
