def main():
    file = open('multiple_lines.txt', 'w')
    file.write('This is a sample text file.\nThis is second line.\n')
    file.write('This is the last line.\n')
    file.close()

main()
