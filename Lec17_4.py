from random import *

n = randint(4,7)
print(f'N:{n}')
abc = n * 2 -2
for i in range(n):
    for j in range(i):
        print (' ', end='')
    print(i+1, end='')
    for j in range(abc):
        print (' ', end='')
    print(i+1)
    abc = abc - 2
