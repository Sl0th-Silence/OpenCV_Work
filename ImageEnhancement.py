import cv2
import matplotlib.pyplot as plt
import numpy as np

# Image enhancement
img_bgr = cv2.imread("sceneryImg.jpg", cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)


matrix = np.ones(img_rgb.shape, dtype="uint8") * 50

img_rgb_brighter = cv2.add(img_rgb, matrix)
img_rgb_darker = cv2.subtract(img_rgb, matrix)

print("Matrix: ", matrix)

plt.figure(figsize=[18, 5])
plt.subplot(131); plt.imshow(img_rgb_darker); plt.title("Darker")
plt.subplot(132); plt.imshow(img_rgb); plt.title("Original")
plt.subplot(133); plt.imshow(img_rgb_brighter); plt.title("Brighter")


# Contrasting
matrix_dark = np.ones(img_rgb.shape) * 0.8
matrix_light = np.ones(img_rgb.shape) * 1.2

img_rgb_darker = np.uint8(cv2.multiply(np.float64(img_rgb), matrix_dark))
img_rgb_lighter = np.uint8(np.clip(cv2.multiply(np.float64(img_rgb), matrix_light), 0, 255))

plt.figure(figsize=[18,5])
plt.subplot(131); plt.imshow(img_rgb_darker);  plt.title("Lower Contrast")
plt.subplot(132); plt.imshow(img_rgb);         plt.title("Original")
plt.subplot(133); plt.imshow(img_rgb_brighter);plt.title("Higher Contrast")

plt.show(block=True)