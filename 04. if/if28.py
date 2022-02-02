yil = int(input("yil = "))
kun = 365 
if yil % 400 == 0:
    kun = 366
elif yil % 4 == 0 and yil % 100 != 0:
    kun = 366
else:
    kun = 365
print(f"{yil} yilda {kun} kun bor")