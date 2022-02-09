y = int(input())
y = y - 1984
y = y % 60
d = ["yashil", "qizil", "sariq", "oq", "qora"]
m = ["sichqon","sigir","yo'lbars","quyon","ajdar","ilon","ot","qo'y","maymun", "tovuq", "it", "to'ngiz"]
print(d[y // 12],m[y % 12])