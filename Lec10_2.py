from random import *
def main():
    count_even = 0
    x = 1
    while x <= 100:
        n = randint(1,10)
        if n % 2 == 0:
            count_even = count_even + 1
        x = x + 1
    print ('Even Count: ', count_even)
main()
