# Ladder pattern

from random import *

n = randint(4, 7)
print(f'N:{n}')
for i in range(n):
    for j in range(i):
        print(' ', end='')
    print('|_')
