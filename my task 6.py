from random import*

n = randint(6, 9)
print(f'N:{n}')
temp = n
for i in range(1, n+1):
    for j in range(temp):
        print(" ", end="")
    for k in range(i):
        print(k+1, end="")
    for l in range(i-1, 0, -1):
        print(l, end="")
    print()
    temp -= 1