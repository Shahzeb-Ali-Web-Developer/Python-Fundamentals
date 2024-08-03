def main():
    im1 = open('img1.pgm','r')
    signature = im1.readline()
    message = im1.readline()
    width, height = map(int, im1.readline().split())
    print ('Width: ', width, '\tHeight:', height)
    clrs = im1.readline()
    image = list(map(int, im1.read().split()))
    print('Number of Pixels:', len(image))
    im1.close()

main()

