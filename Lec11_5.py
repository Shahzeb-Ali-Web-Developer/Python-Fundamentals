def main():
    #to read integers from nums
    file = open('nums.txt', 'r')
    i = 1
    while i <= 10:
        n = int(file.readline())
        print(n, end=' ')
        i = i + 1
    print()
    file.close()

main()

