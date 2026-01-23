import cv2
import sys

#Chooses camera device index
camera_device_index = 0
if len(sys.argv) > 1:
    camera_device_index = sys.argv[1]

#Gets video cam
source = cv2.VideoCapture(camera_device_index)

#Create the camera window
win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

#While loop that waits for the escape key.
while cv2.waitKey(1) != 27: #Escape key
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv2.imshow(win_name, frame)

source.release()
cv2.destroyWindow(win_name)