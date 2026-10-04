################################################
#
# COMS30068 - draw.py
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
image[:,:,2] = 255

# put white text HelloOpenCV
image = cv2.putText(image, "HelloOpenCV", (70, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255, 255, 255), 1, cv2.LINE_AA)

# draw blue line under text
image = cv2.line(image, (74, 90), (190, 90), (255, 0, 0), 2)

# draw a green smile 
image = cv2.ellipse(image, (130, 180), (25,25), 180, 180, 360, (0, 255, 0), 2)
image = cv2.circle(image, (130, 180), 50, (0, 255, 0), 2)
image = cv2.circle(image, (110, 160), 5, (0, 255, 0), 2)
image = cv2.circle(image, (150, 160), 5, (0, 255, 0), 2)

# save image to file
cv2.imwrite("myimage.jpg", image)