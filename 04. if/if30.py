x = int(input("x = "))
if x < 10:
    if x % 2 == 0:
        print("bir xonali juft son")
    else:
        print("bir xonali toq son")
elif x < 100:
    if x % 2 == 0:
        print("ikki xonali juft son")
    else:
        print("ikki xonali toq son")
else:
    if x % 2 == 0:
        print("uch xonali juft son")
    else:
        print("uch xonali toq son")