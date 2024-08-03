def main():
    im1 = open('img1.pgm','r')
    im2 = open('img_black_line.pgm','w')
    signature = im1.readline()
    im2.write(signature)
    message = im1.readline()
    im2.write(message)
    width, height = map(int, im1.readline().split())
    im2.write(f'{width} {height}\n')
    clrs = im1.readline()
    im2.write(clrs)
    image = list(map(int, im1.read().split()))
    for i in range(width * 50, width * 55):
        image[i] = 0
    im2.write(str(image))
    im1.close()
    im2.close()

main()

