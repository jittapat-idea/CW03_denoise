import cv2 
import random
import numpy as np
from skimage.metrics import structural_similarity as ssim


img_no_noise = cv2.imread('pic/Durga.png',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('pic/Durga.png',cv2.IMREAD_GRAYSCALE)

# img_no_noise = cv2.imread('pic/anime1.jpeg',cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('pic/anime1.jpeg',cv2.IMREAD_GRAYSCALE)

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


# def calculate_snr(image_with_noise, image_without_noise):
#     signal_power = np.sum(np.square(image_without_noise))
#     noise_power = np.sum(np.square(image_with_noise - image_without_noise))
#     snr = 10 * np.log10(signal_power / noise_power)
#     return snr
# snr = calculate_snr(img, img_no_noise)
# print("snr = ", snr)

# histogram = cv2.calcHist([img],[0],None,[256],[0,256])
# histogram = cv2.calcHist([img_no_noise],[0],None,[256],[0,256])
# print("histogram = ",histogram)

def อยากจะเบรอก็โทรมา(รูปไม่สะอาด,รูปสะอาด):
    max_score = 0.8  # ค่าคะแนนสูงสุดที่ได้รับจาก SSIM
    best_blur_value = None  # ค่าที่ใช้ในการทำ MedianBlur ที่ให้คะแนนสูงสุด

    for blur_value in range(1, 10,2):
        เเก้รูปกันเถอะ = cv2.medianBlur(รูปไม่สะอาด,blur_value)
        score = ssim(เเก้รูปกันเถอะ, รูปสะอาด, multichannel=True)  # ใช้ SSIM เพื่อวัดความคล้ายคลึงระหว่างภาพ
        print("คะเเนน = ", score)
        if score > max_score:
            print("ค่า เบรอ = ", blur_value)
            combined_image = cv2.hconcat([img_no_noise, เเก้รูปกันเถอะ ])
            cv2.imshow("Original vs Filtered", combined_image)
            # cv2.imwrite('pic/Durga_no_noise.png',combined_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

# def อยากจะเบรอก็โทรมา(รูปไม่สะอาด,รูปสะอาด):
#     max_score = []  # ค่าคะแนนสูงสุดที่ได้รับจาก SSIM
#     best_blur_value = []  # ค่าที่ใช้ในการทำ MedianBlur ที่ให้คะแนนสูงสุด

#     for blur_value in range(1, 10,2):
#         เเก้รูปกันเถอะ = cv2.medianBlur(รูปไม่สะอาด,blur_value)
#         score = ssim(เเก้รูปกันเถอะ, รูปสะอาด, multichannel=True)  # ใช้ SSIM เพื่อวัดความคล้ายคลึงระหว่างภาพ
#         max_score.append(score)
#         best_blur_value.append(blur_value)

#     for x in max_score:
#         if max_score[x] == max(max_score):
#             คะเเนนสูงสุด = best_blur_value[x]
#             print('คะเเนนสูงสุด = ' ,คะเเนนสูงสุด)
    
#     image = cv2.medianBlur(รูปไม่สะอาด,คะเเนนสูงสุด)
#     combined_image = cv2.hconcat([img_no_noise, image ])
#     cv2.imshow("Original vs Filtered", combined_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

อยากจะเบรอก็โทรมา(img ,img_no_noise)


