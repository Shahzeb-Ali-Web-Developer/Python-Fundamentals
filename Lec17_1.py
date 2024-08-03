from random import *

n = randint(4,7)
print(n)
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(j, end='')
        k = 1
        if j < n:
            while k <= i:
                print(end='*')
                k = k + 1
        j = j + 1
    print()
    i = i + 1
