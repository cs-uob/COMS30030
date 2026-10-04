################################################
#
# COMS30068 - RGBtoGRAY.py
# University of Bristol
#
################################################

import numpy as np
import cv2
import os
import sys
import argparse

# LOADING THE IMAGE
# Example usage: python RGBtoGRAY.py -n mandrillRGB.jpg
parser = argparse.ArgumentParser(description='Convert RGB to GRAY')
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
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY )
cv2.imwrite("gray.jpg", gray_image)