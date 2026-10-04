################################################
#
# COMS30068 - RGBtoHSV.py
# University of Bristol
#
################################################

import numpy as np
import cv2
import os
import sys
import argparse

# LOADING THE IMAGE
# Example usage: python RGBtoHSV.py -n mandrillRGB.jpg
parser = argparse.ArgumentParser(description='Convert RGB to HSV')
parser.add_argument('-name', '-n', type=str)
args = parser.parse_args()
imageName = args.name

# ignore if no such file is present.
if not os.path.isfile(imageName):
    print('No such file')
    sys.exit(1)

# Read image from file
image = cv2.imread(imageName, 1)

# ignore if image is not array.
if not (type(image) is np.ndarray):
    print('Not image data')
    sys.exit(1)

# CONVERT COLOUR AND SAVE
image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV )
cv2.imwrite("hsv.jpg", image)