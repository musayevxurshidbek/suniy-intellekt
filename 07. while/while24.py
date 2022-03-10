n = int(input('n = '))
f1 = 1
f0 = 0
fn = f1 + f0
while fn < n:
    f0 = f1
    f1 = fn
    fn = f1 + f0

if fn == n:
    print("Fibonachi soni")
else:
    print("Fibonachi soni emas")