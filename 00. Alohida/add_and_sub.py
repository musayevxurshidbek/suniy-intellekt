def main():
    # kiritish
    a = float(input("a = "))
    b = float(input("b = "))
    amal = int(input("1 - (*), 2 - (/) =>"))
    if (a < 0 and b < 0) or (a > 0 and b > 0):
        ishora = False
    else:
        ishora = True
    a = abs(a)
    b = abs(b)
    surat_a = a
    mahraj_a = 1
    surat_b = b
    mahraj_b = 1

    # a sonini kasrga aylantirish
    while surat_a != int(surat_a):
        surat_a += a
        mahraj_a += 1
    surat_a = int(surat_a)
    surat_a, mahraj_a = qisqartir(surat_a, mahraj_a, ekub(surat_a, mahraj_a))
    # print(surat_a, mahraj_a, sep="/")
    # b sonini kasrga aylantirish
    while surat_b != int(surat_b):
        surat_b += b
        mahraj_b += 1
    surat_b = int(surat_b)
    surat_b, mahraj_b = qisqartir(surat_b, mahraj_b, ekub(surat_b, mahraj_b))
    # print(surat_b, mahraj_b, sep="/")
    if amal == 1:
        # ko'paytirish
        surat_a, mahraj_b = qisqartir(surat_a, mahraj_b, ekub(surat_a, mahraj_b))
        mahraj_a, surat_b = qisqartir(mahraj_a, surat_b, ekub(mahraj_a, surat_b))
        surat_res = mul_x_y(surat_a, surat_b)
        mahraj_res = mul_x_y(mahraj_a, mahraj_b)
    else:
        # bo'lish
        surat_a, surat_b = qisqartir(surat_a, surat_b, ekub(surat_a, surat_b))
        mahraj_a, mahraj_b = qisqartir(mahraj_a, mahraj_b, ekub(mahraj_a, mahraj_b))
        surat_res = mul_x_y(surat_a, mahraj_b)
        mahraj_res = mul_x_y(mahraj_a, surat_b)

    butun, qoldiq = x_div_mod_y(surat_res, mahraj_res)
    kasr = 0
    hona = 0
    while qoldiq != 0 and hona != 7:
        hona += 1
        surat_res = mul_x_y(qoldiq, 10)
        k, qoldiq = x_div_mod_y(surat_res, mahraj_res)
        kasr = mul_x_y(kasr, 10) + k

    kasr, k = x_div_mod_y(kasr, 10)
    if k > 5 and hona > 6:
        kasr += 1

    x = 1e-1 if hona == 1 else 1e-2 if hona == 2 else 1e-3 if hona == 3 else 1e-4 if hona == 4 else 1e-5 if hona == 5 else 1e-6
    son_kasr = 0
    for _ in range(0, kasr):
        son_kasr += x

    son = butun + son_kasr
    if ishora:
        son = -son

    print(son)


def ekub(n, m):
    while n != m:
        if n > m:
            n -= m
        else:
            m -= n
    return n


def x_div_mod_y(x, y):
    res = 0
    while x >= y:
        x -= y
        res += 1
    return res, x


# x va z sonlarini z ga qisqartirish
def qisqartir(x, y, z):
    if z > 1:
        s = 0
        while x != 0:
            x -= z
            s += 1
        x = s
        s = 0
        while y != 0:
            y -= z
            s += 1
        y = s
    return x, y


def mul_x_y(x, y):
    res = 0
    if x <= y:
        while x != 0:
            res += y
            x -= 1
    else:
        while y != 0:
            res += x
            y -= 1
    return res


if __name__ == "__main__":
    main()
