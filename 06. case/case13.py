from math import sqrt

print("1 - Katet, 2 - Gipotenuza,\n3 - Balandlik, 4 - Yuza")
a = int(input("Birini kiriting: "))
d = "Katet" if a == 1 else "Gipotenuza" if a == 2 else "Balandlik" if a == 3 else "Yuza"
x = float(input(f"{d}ni kiriting: "))
if a == 1:
    c = sqrt(2) * x
    h = c / 2
    s = c * h / 2
    print(f"Gipotenuza - {c},Balandlik - {h}, Yuza - {s}")
elif a == 2:
    c = x / sqrt(2)
    h = x / 2
    s = x * h / 2
    print(f"Katet - {c},Balandlik - {h}, Yuza - {s}")
elif a == 3:
    c = x * sqrt(2)
    h = 2 * x
    s = x * h / 2
    print(f"Katet - {c},Gipotenuza - {h}, Yuza - {s}")
else:
    c = sqrt(2 * x)
    h = sqrt(2) * c
    s = h / 2
    print(f"Katet - {c},Gipotenuza - {h}, Balandlik - {s}")
