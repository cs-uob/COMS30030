################################################
#
# COMS30068 - thr.py
# TOPIC: create, save and display an image
#
# Getting-Started-File for OpenCV
# University of Bristol
#
################################################

import cv2
import numpy as np

# Read image from file
image = cv2.imread("mandrill.jpg", 1)

# Convert to grey scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )

# Create mask from threshold 
th = 128
gray_image = gray_image>128
gray_image = gray_image*255

# Or threshold by looping through all pixels
# for y in range(0, image.shape[0]):  # go through all rows (or scanlines)
#	for x in range(0, image.shape[1]):  # go through all columns
#		if gray_image[y, x] > 128:
#			gray_image[y, x] = 255
#		else:
#			gray_image[y, x] = 0


# Save thresholded image
cv2.imwrite("thr.jpg", gray_image)