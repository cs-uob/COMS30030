################################################
#
# COMS30068 - pixels.py
# TOPIC: create, save and display an image
#
# Getting-Started-File for OpenCV
# University of Bristol
#
################################################

import cv2
import numpy as np

# create a red 256x256, 8bit, 3channel BGR image in a matrix container
image = np.zeros([256,256,3], dtype=np.uint8)

# set pixels to create colour pattern

for y in range(0, image.shape[0]):  # go through all rows (or scanlines)
	for x in range(0, image.shape[1]):  # go through all columns
		image[y, x, 0] = x # set blue component
		image[y, x, 1] = y # set green component  
		image[y, x, 2] = 255 - image[y, x,1] # set red component

# construct a window for image display
namedWindow = 'Display window'

# visualise the loaded image in the window
cv2.imshow(namedWindow, image)

# wait for a key press until returning from the programw
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()