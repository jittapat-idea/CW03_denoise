import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('pic/Gonzo.jpeg',cv2.IMREAD_GRAYSCALE)

histogram = cv2.calcHist([image],[0],None,[256],[0,256])
print("histogram = ",histogram)

# image2 = cv2.medianBlur(image,5)

# histogram = cv2.calcHist([image2],[0],None,[256],[0,256])
# print("histogram = ",histogram)

plt.plot(histogram,color='k')

plt.xlim([0,256])
plt.grid(True)

mean = np.mean(image)
print('mean', mean)

plt.title('Histogram of image')
plt.ylabel('Number of Pixels')
plt.xlabel('Intensity levels')

plt.show()