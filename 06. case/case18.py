a = int(input("Son kiriting: "))
a0 = a // 100
a1 = a % 100 // 10
a2 = a % 10
if a0 == 1:
    s = "bir yuz "
elif a0 == 2:
    s = "ikki yuz "
elif a0 == 3:
    s = "uch yuz "
elif a0 == 4:
    s = "to'rt yuz "
elif a0 == 5:
    s = "besh yuz "
elif a0 == 6:
    s = "olti yuz "
elif a0 == 7:
    s = "yetti yuz "
elif a0 == 8:
    s = "sakkiz yuz "
elif a0 == 9:
    s = "to'qqiz yuz "
else:
    s = ""

if a1 == 1:
    s += "o'n "
elif a1 == 2:
    s += "yigirma "
elif a1 == 3:
    s += "o'ttiz "
elif a1 == 4:
    s += "qirq "
elif a1 == 5:
    s += "ellik "
elif a1 == 6:
    s += "oltmish "
elif a1 == 7:
    s += "yetmish "
elif a1 == 8:
    s += "sakson "
elif a1 == 9:
    s += "to'qson "
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
print(s, "ta masala", sep="\b")
