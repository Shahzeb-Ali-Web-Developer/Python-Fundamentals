from random import *

def main():
    x = randint(10, 100)
    print ('X: ', x)
    d = 2
    while d <= x:
        if x % d == 0:
            print (f'{x} is divisible by {d}')
        d = d + 1
main()