a = float(input("a = "))
b = float(input("b = "))
amal = int(input("Amal 1-(+),2-(-),3-(*),4-(/) => "))
if a == 1:
    print(a+b)
elif a == 2:
    print(a-b)
elif a == 3:
    print(a*b)
else:
    if b !=0:
        print(a / b)
    else:
        print("O ga bo'lish mumkin emas")