k = int(input("1-kg,2-mg,3-g,4-t,5-s. Birini kiriting: "))
f = float(input("Tanlangan birlikda qiymat kiriting: "))
f *= 1 if k == 1 else 1e-6 if k == 2 else 1e-3 if k == 3 else 1e3 if k == 4 else 100
print(f)