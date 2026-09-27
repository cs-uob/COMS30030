################################################
#
# COMS30076 - colourthr.py
# University of Bristol
#
################################################

import cv2
import numpy as np

image = cv2.imread("darkBristol.png", 1)

# enhance brightness
image = np.power(image, 1.5)

cv2.imwrite("enhancedBristol.jpg", image)

