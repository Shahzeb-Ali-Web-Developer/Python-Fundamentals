file = open('matrix.txt', 'r')
rows = int (file.readline())
columns = int (file.readline())
i = 1
while i <= rows:
    j = 1
    while j <= columns:
        n = int (file.readline())
        print (n, end=' ')
        j = j + 1
    print()
    i = i + 1

