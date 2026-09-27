################################################
#
# COMS30068 - colourthr.py
# University of Bristol
#
################################################

import cv2
import numpy as np

# reorder channels
image = cv2.imread("mandrill0.jpg", 1)
idx = [2, 0, 1]
cv2.imwrite("recon0.jpg", image[:,:,idx])

# translate red channel
image = cv2.imread("mandrill1.jpg", 1)
image[:,:,2] = np.roll(image[:,:,2], 30)
image[31:,:,2] = image[:481,:,2]
cv2.imwrite("recon1.jpg", image)

# inverse colours
image = cv2.imread("mandrill2.jpg", 1)
cv2.imwrite("recon2.jpg", 255-image)

# convert colours
image = cv2.imread("mandrill3.jpg", 1)
image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR )
cv2.imwrite("recon3.jpg", image)