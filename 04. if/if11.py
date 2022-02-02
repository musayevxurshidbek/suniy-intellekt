a = int(input("a = "))
b = int(input("b = "))
if a != b:
	c = max(a,b)
	a,b = c,c
else:
	a,b = 0,0
print(a,b)