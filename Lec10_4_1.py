from random import *

def main():
    n1 = randint(1,100)
    n2 = randint(1,100)
    print (f'N1: {n1}\tN2: {n2}    N1 & N2 are printing to check the code only')
    if n1 < n2:
        while n1 <= n2:
            print (n1, end = ' ')
            n1 = n1 + 1
    else:
        while n2 <= n1:
            print (n2, end = ' ')
            n2 = n2 + 1
main()

