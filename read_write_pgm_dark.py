def main():
    im1 = open('img1.pgm','r')
    im2 = open('img2.pgm','w')
    signature = im1.readline()
    im2.write(signature)
    message = im1.readline()
    im2.write(message)
    width, height = map(int, im1.readline().split())
    im2.write(f'{width} {height}\n')
    clrs = im1.readline()
    im2.write(clrs)
    image = list(map(int, im1.read().split()))
    for i in range(width * height):
        image[i] = image[i] // 4
    im2.write(str(image))
    im1.close()
    im2.close()

main()

