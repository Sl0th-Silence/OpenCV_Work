import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("sceneryImg.jpg", cv2.IMREAD_COLOR)
img_reversed = img
plt.imshow(img_reversed)

cropped_area = img_reversed[1000:1500, 1000:2000]
# flipped = cv2.flip(cropped_area, 0)
plt.imshow(cropped_area)

img_line = img.copy()
# Draw a line
cv2.line(img_line, (200, 200), (2500, 600), (255, 0, 255), thickness=5, lineType=cv2.LINE_AA)
plt.imshow(img_line[:,:,::-1])

# Draw a circle
img_circle = img.copy()
cv2.circle(img_circle, (1000, 600), 200, (0, 255, 255), thickness=10, lineType=cv2.LINE_AA)
plt.imshow(img_circle[:,:,::-1])

plt.figure()
# Draw a rectangle
# Start point is top left, second point is botton right
# 1000 500, 1500 1250

img_rect = img.copy()
cv2.rectangle(img_rect, (1000, 500), (1500, 1250), (255, 255, 255), thickness=-2, lineType=cv2.LINE_8)
cv2.rectangle(img_rect, (2000, 500), (2500, 1250), (255, 255, 255), thickness=-2, lineType=cv2.LINE_8)
plt.imshow(img_rect[:, :, ::-1])

img_text = img.copy()
phrase = "This is my first annotation!"
font_scale = 5
font_face = cv2.FONT_HERSHEY_TRIPLEX
font_color = (0, 0, 0)
font_thickness = 15

cv2.putText(img_text, phrase, (1000, 1500), font_face, font_scale, font_color, font_thickness, lineType=cv2.LINE_AA)
#plt.imshow(img_text[:,:,::-1])



plt.show(block=True)