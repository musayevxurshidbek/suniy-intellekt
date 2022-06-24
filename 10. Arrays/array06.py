# 1 - usul
n = int(input("n = "))
a = int(input("a = "))
b = int(input("b = "))
ar = [a,b]
if n >= 2:
    ar.append(a+b)
for i in range(3,n + 1):
    ar.append(2 ** (i - 2) * (a + b))
print(ar)

# # 6m 2 - usul
# def sum(a,x):
#     if x == 0:
#         return 0
#     else:
#         return ar[x - 1] + sum(a,x-1)
#
# n = int(input("n = "))
# a = int(input("a = "))
# b = int(input("b = "))
# ar = [a,b]
# for i in range(2,n+1):
#     ar.append(sum(ar,i))
# print(ar)