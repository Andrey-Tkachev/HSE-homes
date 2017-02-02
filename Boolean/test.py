res = 0.0
x = 4
k = 1.0
for i in range(6):
    res += k * x
    k = (abs(k) + 1.0) * ((-1) ** (i + 1))
    print(res)
