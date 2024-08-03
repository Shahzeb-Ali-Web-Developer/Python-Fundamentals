file = open('matrix.txt', 'r')
rows = int (file.readline())
columns = int (file.readline())
i = 1
while i <= rows * columns:
    n = int (file.readline())
    print (n, end=' ')
    i = i + 1
file.close()
