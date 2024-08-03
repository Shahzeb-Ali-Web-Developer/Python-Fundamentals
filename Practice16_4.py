from random import *

def main():
    a = randint(1, 100)
    b = randint(1, 100)
    c = randint(1, 100)
    d = randint(1, 100)
    e = randint(1, 100)
    print (f'Element 1: {a}\nElement 2: {b}\nElement 3: {c}\nElement 4: {d}\nElement 5: {e}');
    print ('Difference of element 1: ', end = ' ')
    difference = a - b
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = a - c
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = a - d
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = a - e
    if difference < 0:	difference = - difference;
    print (difference)
    print ('Difference of element 2: ', end = ' ')
    difference = b - a;
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = b - c;
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = b - d;
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = b - e;
    if difference < 0:	difference = - difference;
    print (difference)
    print ('Difference of element 3: ', end = ' ')
    difference = c - a
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = c - b
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = c - d
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = c - e
    if difference < 0:	difference = - difference;
    print (difference)
    print ('Difference of element 4: ', end = ' ')
    difference = d - a
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = d - b
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = d - c
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = d - e
    if difference < 0:	difference = - difference;
    print (difference)
    print ('Difference of element 5: ', end = ' ')
    difference = e - a;
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = e - b;
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = e - c
    if difference < 0:	difference = - difference;
    print (difference, end = '  ')
    difference = e - d
    if difference < 0:	difference = - difference;
    print (difference)

main()