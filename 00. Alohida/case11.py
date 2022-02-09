y = input("y = ")
k1 = input("k1 = ")
k2 = input("k2 = ")

if k1 == 1:
    print("s" if y == "q" else "q" if y == "j" else "j" if y == "g" else "g")
elif k1 == 0:
    print("s" if y == "g" else "g" if y == "j" else "j" if y == "q" else "q")
else:
    print("s" if y == "j" else "j" if y == "s" else "q" if y == "g" else "g")

if k2 == 1:
    print("s" if y == "q" else "q" if y == "j" else "j" if y == "g" else "g")
elif k2 == 0:
    print("s" if y == "g" else "g" if y == "j" else "j" if y == "q" else "q")
else:
    print("s" if y == "j" else "j" if y == "s" else "q" if y == "g" else "g")