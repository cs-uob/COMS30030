################################################
#
# COMS30076 - colourthr.py
# University of Bristol
#
################################################

import cv2
import numpy as np

# Read image from file
image = cv2.imread("mandrillRGB.jpg", 1)


nose = cv2.inRange(image, (0, 0, 200), (120, 100, 255))
cv2.imwrite("nose.jpg", nose)

cheek = cv2.inRange(image, (200, 100, 0), (255, 200, 160))
cv2.imwrite("cheek.jpg", cheek)