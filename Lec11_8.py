def main():
    file = open('nums.txt', 'r')
    i = 1
    #while loop to skip first five lines
    while i <= 5:
        file.readline()
        i = i + 1
    i = 1
    #while loop to read next five lines
    while i <= 5:
        n = int(file.readline())
        print(n, end=' ')
        i = i + 1
    print()
    file.close()

main()# Write your code here :-)
