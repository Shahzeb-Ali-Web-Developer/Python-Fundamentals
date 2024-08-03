from random import*

n = randint(1, 6)
print("number : ", n)
temp = (n - 1) * 2
for i in range(1, n+1):
    for j in range(i-1):
        print(" ", end="")
    print(i, end="")
    for k in range(temp):
        print(" ", end="")
    print(i)
    temp -= 2
