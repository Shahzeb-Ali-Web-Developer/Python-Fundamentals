from random import *
def main():
    sum = 0
    x = 1
    while x <= 100:
        n = randint(1,9)
        sum = sum + n
        x = x + 1
    print ('Sum: ', sum)
main()
