from random import*
LENGTH = randint(5,9)
d = [[randint(1,9) for i in range(LENGTH)] for j in range(LENGTH)]
for i in range(LENGTH):
    d[i][i] = 0 
for i in range(LENGTH):
    for j in range(LENGTH):
        print(d[i][j], end=' ')
    print()

def main(d, city1, city2):
    short = 9999
    print('Direct Distance:', d[city1][city2])
    print('Indirect Distance')
    if short > d[city1][city2]:
        short = d[city1][city2]
    for i in range(LENGTH):
        if i != city1 and i != city2:
            ind = d[city1][i] + d[i][city2]
            print(f'Via City {i}: {ind}')
            if short > ind:
                short = ind
    if short == ind:
        print(f'City{city1} and City{city2} has shortest distance Via City {i}, {short}')
    elif short == d[city1][city2]:
        print(f'City{city1} and City{city2} has shortest distance {short}')
main(d, 1, 3)
for i in range (LENGTH):
    mn = 9999
    for j in range (LENGTH):
        if i != j:
            dir = d[i][j]
            if mn > dir:
                mn = dir
                c1 = i
                c2 = j
print(f'City{c1} and City{c2} have shortest direct distance {mn}')  

