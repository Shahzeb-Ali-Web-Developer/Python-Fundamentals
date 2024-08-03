from random import *

def main():
    table_no = randint(1,100)
    i = 1
    while i <= 10:
        print (f'{table_no}\t*\t{i}\t=\t{table_no*i}')
        i = i + 1
main()

