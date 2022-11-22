b = ['', 'bir ', 'ikki ', 'uch ', 'to\'rt ', 'besh ', 'olti ', 'yetti ', 'sakkiz ', 'to\'qqiz ']
u = ['', 'o\'n ', 'yigirma ', 'o\'ttiz ', 'qirq ', 'ellik ', 'oltmish ', 'yetmish ', 'sakson ', 'to\'qson ']
m = ['','ming ', 'million ', 'milliard ','trillion ', 'kvadrillion ', 'kvintillion ','sektillion ','septillion ']


def minglik(x):
    a1 = x // 100
    a2 = x % 100 // 10
    a3 = x % 10
    s = ''
    if a1 > 0:
        s = b[a1] + 'yuz '
    s += u[a2]
    s += b[a3]
    return s

k = int(input('k = '))
g = ""
f = 0
while k != 0:
    h = k % 1000
    if h > 0:
        g = minglik(h) + m[f] + g
    f += 1
    k = k // 1000
print(g)
