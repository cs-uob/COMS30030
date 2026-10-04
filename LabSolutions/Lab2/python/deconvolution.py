
################################################
#
# COMS30068 - deconvolution.py
# TOPIC: Advanced Wiener Deconvoluition
#
# Getting-Started-File for OpenCV
# University of Bristol
#
#
# Function  that performs Wiener Deconvolution on an image
#
# Requires: An input image to be deconvolved
#           An output image to hold the results
#           The estimated length of the blur kernel
#           The estimated angle of the blur
#           An estimated noise to signal ratio
#
################################################

import numpy as np
import cv2
import os
import sys
import argparse

# LOADING THE IMAGE
# Example usage: python deconvolution.py -n car1.png
parser = argparse.ArgumentParser(description='Convert RGB to GRAY')
parser.add_argument('-name', '-n', type=str, default='car3.png')
args = parser.parse_args()

# ==================================================
# THIS FUNCTION PROVIDES AN IMPLEMENTATION OF
# WIENER DECONVOLUTION FOR YOU

def WienerDeconvoluition(input, motionLength, motionAngle, noiseSignalRatio, displayPowerSpectrums):
	'''
	 * Given the length of the blur and
	 * the angle to blur it at we need to create
	 * an appropriate kernel
	'''
	length = motionLength;
	angle = motionAngle;

	# make sure that the length is odd so the line
	# can be positioned at a center value
	if (length % 2 == 0):
		length += 1

	xdim = length;
	ydim = length;

	# create the kernel
	tempKernel = np.zeros([xdim,ydim])

	# find the index of the centre row
	rowIndex = round(np.floor(length / 2))

	# draw a horizontal line into the kernel
	tempKernel[rowIndex,:] = 1

	# set the end points
	tempKernel[rowIndex, 0] = 0.5
	tempKernel[rowIndex, length - 1] = 0.5

	# create a rotation matrix to rotate the line
	# so it matches the angle
	rotationMatrix = cv2.getRotationMatrix2D(center=(rowIndex,rowIndex), angle=angle, scale=1)

	# rotate the kernel
	kernel = cv2.warpAffine(tempKernel, rotationMatrix, (tempKernel.shape[0],tempKernel.shape[1]))

	# normalise the kernel
	kernel = kernel/kernel.sum()

	# Here we need to prepare the input and the kernel
	# by making sure they are the correct size, then
	# doing a dft on them
	m =  input.shape[0] # cv::getOptimalDFTSize( input.rows );
	n =  input.shape[1] # cv::getOptimalDFTSize( input.cols );
		
		# pad both the kernel and the image so they are the correct size
	paddedInput = cv2.copyMakeBorder(input, 
		0, m - input.shape[0], 0, n - input.shape[1], 
		cv2.BORDER_CONSTANT, 0)

	paddedKernel = cv2.copyMakeBorder(kernel, 
		0, m -kernel.shape[0], 0, n - kernel.shape[1], 
		cv2.BORDER_CONSTANT, 0)

	# do the dft on the image
	inputFFT = cv2.dft(np.float32(paddedInput), flags = cv2.DFT_COMPLEX_OUTPUT)

	# do the dft on the kernel
	kernelFFT = cv2.dft(np.float32(paddedKernel), flags = cv2.DFT_COMPLEX_OUTPUT)

	if displayPowerSpectrums:
		'''
		// the fft output needs to be split into complex
		// and real parts, then the magnitude taken.
		// Finally, the log is taken and then the result
		// normalised to make it displayable
		'''

		kernelMag = cv2.magnitude(kernelFFT[:,:,0], kernelFFT[:,:,1]) + 1
		kernelMag = cv2.log(kernelMag)
		kernelMag = (kernelMag - kernelMag.min())/(kernelMag.max() - kernelMag.min())
		cv2.imshow("Kernel Magnitude", np.uint8(255*kernelMag))

		imageMag = cv2.magnitude(inputFFT[:,:,0], inputFFT[:,:,1]) + 1
		imageMag = cv2.log(imageMag)
		imageMag = (imageMag - imageMag.min())/(imageMag.max() - imageMag.min())
		imshow("Image Magnitude", np.uint8(255*imageMagimageMag))

	
	# Now we do the convolution by visiting each pixel, and
	# computing the Wiener Deconvolution function
	Su = noiseSignalRatio
	Sx = 1
	H = kernelFFT[...,0] + 1j * kernelFFT[...,1]
	I = inputFFT[...,0] + 1j * inputFFT[...,1]
	normH = np.abs(H)**2
	denominator = normH + ( Su / ( Sx - Su ) )
	responseFFT = I * (np.conjugate(H) / denominator)

	# check the denominator is above an approximation of 0
	mask = np.abs(denominator) > 1.0e-4 
	responseFFT = responseFFT * mask

	'''
	# Try like cpp
	# Now we do the convolution by visiting each pixel, and
	# computing the Wiener Deconvolution function
	responseFFT = np.zeros([inputFFT.shape[0],inputFFT.shape[1]], dtype=np.complex)
	for i in range(0, inputFFT.shape[0]):
		for j in range(0, inputFFT.shape[1]):
			H = kernelFFT[i,j,0] + 1j * kernelFFT[i,j,1]
			I = inputFFT[i,j,0] + 1j * inputFFT[i,j,1]
			denominator = np.abs(H)**2 + ( Su / ( Sx - Su ) )
			value = 0.
			if( np.abs( denominator )  > 1.0e-4 ):
				value = I * (np.conjugate(H) / denominator)
				responseFFT[i ,j] = value;
	'''

	# Now we take the inverse of the response to the deconvolution
	responseFFT = np.array(np.dstack([responseFFT.real,responseFFT.imag]))
	#outputUncropped = cv2.idft(responseFFT, cv2.DFT_INVERSE + cv2.DFT_REAL_OUTPUT+ cv2.DFT_SCALE, input.shape[0])
	outputUncropped = cv2.idft(responseFFT, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
	# normalise the output to be within the uchar range
	outputUncropped = (outputUncropped - outputUncropped.min())/(outputUncropped.max() - outputUncropped.min())

	return (outputUncropped*255).astype(np.uint8)


# ==== MAIN ==============================================
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

# CONVERT COLOUR, BLUR AND SAVE
gray_image = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY )
gray_image = gray_image.astype(np.float32)

# ADJUST THIS FUNCTION CALL
recover = WienerDeconvoluition(gray_image,15,3,0.001,0)
# save image
cv2.imwrite( "recover.jpg", recover );








