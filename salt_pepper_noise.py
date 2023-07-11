import cv2 
import random

img = cv2.imread('pic/Durga.png',cv2.IMREAD_GRAYSCALE)

density_sait = 0.1
density_pepper = 0.1

number_white_pixel = int(density_sait * (img.shape[0] * img.shape[1]))

for i in range(number_white_pixel):
    y = random.randint(0,img.shape[0] - 1)
    x = random.randint(0,img.shape[1] - 1)
    img[y][x] = 255

number_black_pixel = int(density_pepper * (img.shape[0] * img.shape[1]))

for i in range(number_black_pixel):
    y = random.randint(0,img.shape[0] - 1)
    x = random.randint(0,img.shape[1] - 1)
    img[y][x] = 0

# output = cv2.medianBlur(img,5)
# cv2.imshow('Durga Image', output )
cv2.imshow('Durga Image', img )
cv2.imwrite('pic/Durga_noise.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()