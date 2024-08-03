from random import *

def main():
    n1 = randint(1,100)
    n2 = randint(1,100) + n1 # to get n2 larger than n1
    while n1 <= n2:
        print (n1, end = ' ')
        n1 = n1 + 1
main()

