a = int(input("a = "))
b = int(input("b = "))
for i in range(a, b + 1):
    for k in range(1, i + 2 - a):
        print(i, end=",")
    print()
