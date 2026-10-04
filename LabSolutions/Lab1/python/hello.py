################################################
#
# COMS30068 - hello.py
# TOPIC: create, save and display an image
#
# Getting-Started-File for OpenCV
# University of Bristol
#
################################################

import cv2
import numpy as np

# create a black 256x256, 8bit, gray scale image in a matrix container
image = np.zeros([256,256], dtype=np.uint8)

# drawwhite text HelloOpenCV!
image = cv2.putText(image, "HelloOpenCV!", (70, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255, 255, 255), 1, cv2.LINE_AA)

# save image to file
cv2.imwrite("myimage.jpg", image)

# construct a window for image display
namedWindow = 'Display window'

# visualise the loaded image in the window
cv2.imshow(namedWindow, image)

# wait for a key press until returning from the programw
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()