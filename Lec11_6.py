def main():
    #to read alternate integers from nums
    file = open('nums.txt', 'r')
    i = 1
    while i <= 5:
        n = int(file.readline())
        print(n, end=' ')
        #next line will skip next line by reading even line
        file.readline()
        i = i + 1
    print()
    file.close()

main()
