y = input("y = ")
k = input("k = ")

if k == "0":
    print(y)
elif k == 1:
    print("s" if y == "q" else "q" if y == "j" else "j" if y == "g" else "g")
else:
    print("s" if y == "g" else "g" if y == "j" else "j" if y == "q" else "q")

