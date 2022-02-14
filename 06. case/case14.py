from math import sqrt

print("1 - Tomoni, 2 - Ichki ayl. radiusi,\n3 - Tashqi ayl. radiusi, 4 - Yuza")
t = int(input("Birini kiriting: "))
d = "Tomoni" if t == 1 else "Ichki ayl. radiusi" if t == 2 else "Tashqi ayl. radiusi" if t == 3 else "Yuza"
x = float(input(f"{d}ni kiriting: "))
if t == 1:
    a = x
    r = sqrt(3) * a / 6
    R = 2 * r
    s = sqrt(3) * a ** 2 / 4
    print(f"Ichki ayl. radiusi - {r},Tashqi ayl. radiusi - {R}, Yuza - {s}")
elif t == 2:
    r = x
    a = 2 * sqrt(3) * r
    R = 2 * r
    s = sqrt(3) * a ** 2 / 4
    print(f"Tomoni - {a},Tashqi ayl. radiusi - {R}, Yuza - {s}")
elif t == 3:
    R = x
    r = R / 2
    a = 2 * sqrt(3) * r
    s = sqrt(3) * a ** 2 / 4
    print(f"Tomoni - {a},Ichki ayl. radiusi - {r}, Yuza - {s}")
else:
    s = x
    a = 2 * sqrt(s / sqrt(3))
    r = sqrt(3) * a / 6
    R = 2 * r
    print(f"Katet - {a},Ichki ayl. radiusi - {r},Tashqi ayl. radiusi - {R}")
