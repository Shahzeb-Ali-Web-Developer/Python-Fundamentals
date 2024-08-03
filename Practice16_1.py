from random import *

def main():
    i = 1
    while i <= 10:
        x = randint(0, 49)
        print (x, end = ' ')
        if i == 1:			small1 = x;
        elif i == 2:
        	if small1 > x:	small2 = small1;	small1 = x;	
        	else:			small2 = x;	
        elif small1 > x:	small2 = small1;	small1 = x;
        elif small2 > x:	small2 = x;
        i = i + 1
    print (f'\nSecond Smallest: {small2}')


main()