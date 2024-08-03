def main():
    #to read alternate integers from nums
    file = open('nums.txt', 'r')
    i = 1
    while i <= 5:
        #next statement will skip odd lines that is first, third...
        file.readline()
        #next statement will read even lines that is second, fourth
        n = int(file.readline())
        print(n, end=' ')
        i = i + 1
    print()
    file.close()

main()# Write your code here :-)
