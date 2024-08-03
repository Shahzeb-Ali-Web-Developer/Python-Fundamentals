file = open('matrix.txt', 'r')
rows = int (file.readline())
columns = int (file.readline())
i = 1
total = rows * columns
while i <= total:
    n = int (file.readline())
    print (n, end=' ')
    if i % columns == 0:
        print()
    i = i + 1
file.close()
