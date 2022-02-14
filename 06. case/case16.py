a = int(input("Yosh kiriting: "))
a1 = a // 10
a2 = a % 10
if a1 == 1:
    s = "O'n "
elif a1 == 2:
    s = "Yigirma "
elif a1 == 3:
    s = "O'ttiz "
elif a1 == 4:
    s = "Qirq "
elif a1 == 5:
    s = "Ellik "
elif a1 == 6:
    s = "Oltmish "
elif a1 == 7:
    s = "Yetmish "
elif a1 == 8:
    s = "Sakson "
elif a1 == 9:
    s = "To'qson "
else:
    s = ""

if a2 == 1:
    s += "bir"
elif a2 == 2:
    s += "ikki"
elif a2 == 3:
    s += "uch "
elif a2 == 4:
    s += "to'rt "
elif a2 == 5:
    s += "besh "
elif a2 == 6:
    s += "olti"
elif a2 == 7:
    s += "yetti"
elif a2 == 8:
    s += "sakkiz "
elif a2 == 9:
    s += "to'qqiz "
else:
    if s == "":
        s = "nol"
print(s,"yosh")