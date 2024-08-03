from random import*
LENGTH = randint(5,9)
d = [[randint(1,9) for i in range(LENGTH)] for j in range(LENGTH)]
aa=randint(4,6)
i=0
while i<=aa:
    j=randint(1,LENGTH-1)
    k=randint(1,LENGTH-1)
    if j!=k:
        d[j][k]=-1
        i+=1
for i in range(LENGTH):
    for j in range(LENGTH):
        d[i][i]=0
        print(d[i][j], end=' ')
    print()
for i in range(LENGTH):
    print(f'City {i} has direct distance with ',end='')
    for j in range(LENGTH):
        if i != j:
            if d[i][j] != -1:
                print(j,end=' ')
    print()

        