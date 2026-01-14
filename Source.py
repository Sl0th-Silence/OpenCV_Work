import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image, display

display(Image(filename="pixel.png"))

img = cv2.imread("pixel.png", 0)
print(img)
img[0, 5] = 150


#Show size
print("Size of img is (H/W)", img.shape)
plt.imshow(img, cmap="gray")


#COKE
plt.figure()
coke_img = cv2.imread("Coca-Cola-Emblem.png", 1)
plt.imshow(coke_img)
#This makes the red come out as blue
#This happens because matplotlib uses RBG and openCV uses BGR

coke_img_reversed = coke_img[:,:,::-1]
plt.imshow(coke_img_reversed)

#Working with layers of color
scene_img = cv2.imread("sceneryImg.jpg", cv2.IMREAD_COLOR) #Read color image
b, g, r = cv2.split(scene_img)
plt.figure(figsize=[10, 2])

plt.subplot(141);plt.imshow(r, cmap="gray");plt.title("Red Channel")
plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green Channel")
plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue Channel")

#Merge image
img_merge = cv2.merge((b, g, r))
#add to plot
plt.subplot(144);plt.imshow(img_merge[:,:,::-1]);plt.title("Merged Image")

#change from BRG to RGB
img_color_change = cv2.cvtColor(scene_img, cv2.COLOR_BGR2RGB)

#plt.figure()
plt.title("Normal Image")
plt.imshow(scene_img)

#plt.figure()
plt.title("Reversed")
plt.imshow(scene_img[:,:,::-1])

#plt.figure()
plt.title("Color Change")
plt.imshow(img_color_change)


plt.show(block=True)
