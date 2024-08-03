r = int(input("rows: "))
c = int(input("Cols: "))
l = 1
for i in range(r):
    sum = 0
    k = 1
    for j in range(c):
        if j == c - 1:
            print(f"{k}", end='')
        else:
            print(f"{k}", end='+')
        sum += k
        k += l
    l += 1
    print("=", sum)

