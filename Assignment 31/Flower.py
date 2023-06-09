import cv2
import numpy as np

img = cv2.imread('input/flower_input.jpg',0)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result = np.zeros(img.shape)
mask = np.ones((21, 21))/441

rows, cols = img.shape
for i in range(10, rows - 10):
    for j in range(10, cols - 10):
        if img[i, j]<200:
            small_img = img[i-10:i+11, j-10:j+11]
            result[i, j] = np.sum(small_img * mask)
        else:
            result[i, j] = img[i, j]

cv2.imwrite('output/result_flower.jpg', result)