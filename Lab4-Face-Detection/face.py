################################################
#
# COMS30068 - face.py
# University of Bristol
#
################################################

import numpy as np
import cv2
import os
import sys
import argparse

# LOADING THE IMAGE
# Example usage: python filter2d.py -n car1.png
parser = argparse.ArgumentParser(description='face detection')
parser.add_argument('-name', '-n', type=str, default='images/face1.jpg')
args = parser.parse_args()

# /** Global variables */
cascade_name = "frontalface.xml"


def detectAndDisplay(frame):

	# 1. Prepare Image by turning it into Grayscale and normalising lighting
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    # 2. Perform Viola-Jones Object Detection
    faces = model.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=1, flags=0, minSize=(10,10), maxSize=(300,300))
    # 3. Print number of Faces found
    print(len(faces))
    # 4. Draw box around faces found
    for i in range(0, len(faces)):
        start_point = (faces[i][0], faces[i][1])
        end_point = (faces[i][0] + faces[i][2], faces[i][1] + faces[i][3])
        colour = (0, 255, 0)
        thickness = 2
        frame = cv2.rectangle(frame, start_point, end_point, colour, thickness)


# ************ NEED MODIFICATION ************
def readGroundtruth(filename='groundtruth.txt'):
    # read bounding boxes as ground truth
    with open(filename) as f:
        # read each line in text file
        for line in f.readlines():
            content_list = line.split(",")
            img_name = content_list[0]
            x = float(content_list[1])
            y = float(content_list[2])
            width = float(content_list[3])
            height = float(content_list[4])
            print(str(x)+' '+str(y)+' '+str(width)+' '+str(height))



# ==== MAIN ==============================================

imageName = args.name

# ignore if no such file is present.
if (not os.path.isfile(imageName)) or (not os.path.isfile(cascade_name)):
    print('No such file')
    sys.exit(1)

# 1. Read Input Image
frame = cv2.imread(imageName, 1)

# ignore if image is not array.
if not (type(frame) is np.ndarray):
    print('Not image data')
    sys.exit(1)


# 2. Load the Strong Classifier in a structure called `Cascade'
model = cv2.CascadeClassifier()
if not model.load(cascade_name): # if got error, you might need `if not model.load(cv2.samples.findFile(cascade_name)):' instead
    print('--(!)Error loading cascade model')
    exit(0)


# 3. Detect Faces and Display Result
detectAndDisplay( frame )

# 4. Save Result Image
cv2.imwrite( "detected.jpg", frame )


