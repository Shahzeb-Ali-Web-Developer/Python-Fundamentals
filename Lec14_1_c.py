file = open('matrix.txt', 'r')
rows = int (file.readline())
columns = int (file.readline())
i = 1
count=0
total = rows * columns
while i <= total:
    n = int (file.readline())
    print (n, end=' ')
    count = count + 1
    if count == columns:
        print()
        count = 0
    i = i + 1
file.close()
