from random import *

n = randint(4, 7)
print(n)
for i in range(n):
    for j in range(1, n+1):
        print(j, end='')
        if j < n:
            for k in range(i+1):
                print("*", end='')
    print()
