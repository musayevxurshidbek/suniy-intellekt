k = int(input("1-dm, 2-km,3-m,4-mm,5-sm. Birini kiriting: "))
f = float(input("Tanlangan birlikda qiymat kiriting: "))
f *= 0.1 if k == 1 else 1000 if k == 2 else 1 if k == 3 else 0.001 if k == 4 else 0.01
print(f)