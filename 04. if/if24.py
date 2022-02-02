x = float(input("x = "))

from math import sin

if x > 0:
    y = 2 * sin(x)
else:
    y = x - 6

print(f"y = {y}")