from random import *

def main():
    a = randint(0, 1)
    b = randint(0, 1)
    c = randint(0, 1)
    d = randint(0, 1)
    e = randint(0, 1)
    print (f'{a}  {b}  {c}  {d}  {e}')
    count0 = count1 = 0
    if (a == 0):	count0 =  count0 + 1;
    else:	        count1 =  count1 + 1;
    if (b == 0):	count0 =  count0 + 1;
    else:	        count1 =  count1 + 1;
    if (c == 0):	count0 =  count0 + 1;
    else:	        count1 =  count1 + 1;
    if (d == 0):	count0 =  count0 + 1;
    else:	        count1 =  count1 + 1;
    if (e == 0):	count0 =  count0 + 1;
    else:	        count1 =  count1 + 1;
    print (f'Count of Zeros: ', count0)
    print (f'Count of Ones: ', count1)

main()