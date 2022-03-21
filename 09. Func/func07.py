def invertDigit(x):
    s = 0
    while x > 0:
        q = x % 10
        s = s * 10 +q
        x//=10
    return s

a =int(input("a = "))
print(invertDigit(a))