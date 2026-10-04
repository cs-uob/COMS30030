/////////////////////////////////////////////////////////////////////////////
//
// deconvolution.cpp
// TOPIC: Advanced Wiener Deconvoluition
//
/////////////////////////////////////////////////////////////////////////////

// header inclusion
#include <stdio.h>
#include <opencv/cv.h>        //you may need to
#include <opencv/highgui.h>   //adjust import locations
#include <opencv/cxcore.h>    //depending on your machine setup


using namespace cv;

/**
 * Function  that performs Wiener Deconvolution on an image
 *
 * Requires: An input image to be deconvolved
 *           An output image to hold the results
 *           The estimated length of the blur kernel
 *           The estimated angle of the blur
 *           An estimated noise to signal ratio
 */
void WienerDeconvoluition(
	cv::Mat & input, 
	cv::Mat &output, 
	int motionLength, 
	int motionAngle,
	double noiseSignalRatio,
	bool displayPowerSpectrums);

int main( int argc, char** argv )
{

 // LOADING THE IMAGE
 char* imageName = argv[1];

 Mat image;
 image = imread( imageName, 1 );

 if( argc != 2 || !image.data )
 {
   printf( " No image data \n " );
   return -1;
 }

 // CONVERT COLOUR AND SAVE
 Mat gray_image;
 cvtColor( image, gray_image, CV_BGR2GRAY );
 Mat recover;

 //ADJUST THIS FUNCTION CALL
 WienerDeconvoluition(gray_image,recover,15,3,0.001,0);
 imwrite( "recover.jpg", recover );

 return 0;
}

// THIS FUNCTION PROVIDES AN IMPLEMENTATION OF
// WIENER DECONVOLUTION FOR YOU
void WienerDeconvoluition(cv::Mat & input, 
	cv::Mat &output, 
	int motionLength, 
	int motionAngle, 
	double noiseSignalRatio,
	bool displayPowerSpectrums)
{
	/**
	 * Given the length of the blur and
	 * the angle to blur it at we need to create
	 * an appropriate kernel
	 */
	cv::Mat kernel;
	int length = motionLength;
	int angle = motionAngle;

	// make sure that the length is odd so the line
	// can be positioned at a center value
	if( length % 2 == 0)
	{
		length++;
	}

	int xdim = length;
	int ydim = length;

	// create the kernel
	cv::Mat tempKernel = cv::Mat::zeros(xdim, ydim, CV_64F);

	// find the index of the centre row
	int rowIndex = (int) floor(((double) length) / 2);

	// draw a horizontal line into the kernel
	for(int i = 0; i < length; i++)
	{
		tempKernel.at<double>( rowIndex, i ) = 1;
	}

	// set the end points
	tempKernel.at<double>( rowIndex, 0 ) = 0.5;
	tempKernel.at<double>( rowIndex, length - 1 ) = 0.5;

	//create a rotation matrix to rotate the line
	// so it matches the angle
	cv::Point centerOfRotation( rowIndex,rowIndex );
	cv::Mat rotationMatrix = cv::getRotationMatrix2D( centerOfRotation, angle, 1.0 );

	// rotate the kernel
	cv::warpAffine( tempKernel, kernel, rotationMatrix, tempKernel.size() );

	// normalise the kernel
	double sum = 0.0;
	for(int i = 0; i < length; i++)
	{
		double * rowPtr = kernel.ptr<double>(i);
		for(int j = 0; j < length; j++)
		{
			sum += rowPtr[j];
		}
	}

	for(int i = 0; i < length; i++)
	{
		double * rowPtr = kernel.ptr<double>(i);
		for(int j = 0; j < length; j++)
		{
			rowPtr[j] /= sum;
		}
	}
	

	// Here we need to prepare the input and the kernel
	// by making sure they are the correct size, then
	// doing a dft on them
	int m =  input.rows;// cv::getOptimalDFTSize( input.rows );
	int n =  input.cols; //cv::getOptimalDFTSize( input.cols );

	cv::Mat paddedInput;
	cv::Mat paddedKernel;
	
	// padd both the kernel and the image so they are the correct size
	cv::copyMakeBorder(input, paddedInput, 
		0, m - input.rows, 0, n - input.cols, cv::BORDER_CONSTANT, cv::Scalar(0));

	cv::copyMakeBorder(kernel, paddedKernel, 
		0, m -kernel.rows, 0, n - kernel.cols, cv::BORDER_CONSTANT, cv::Scalar(0));


	// perform the dft on the input and the kernel (must convert to floating point matrixes)
	cv::Mat inputPlanes[] = {cv::Mat_<double>(paddedInput),cv::Mat::zeros(paddedInput.size(), CV_64F)};
	cv::Mat FInput;
	cv::merge(inputPlanes, 2, FInput);
	cv::Mat inputFFT;

	// do the dft on the image
	cv::dft(FInput, inputFFT);

	cv::Mat kernelPlanes[] = {cv::Mat_<double>(paddedKernel), cv::Mat::zeros(paddedKernel.size(), CV_64F)};
	cv::Mat FKernel;
	cv::merge(kernelPlanes, 2, FKernel);
	cv::Mat kernelFFT;

	// do the dft on the kernel
	cv::dft(FKernel, kernelFFT);

	if( displayPowerSpectrums )
	{
		// the fft output needs to be split into complex
		// and real parts, then the magnitude taken.
		// Finally, the log is taken and then the result
		// normalised to make it displayable

		cv::Mat planes1[2];
		cv::split(kernelFFT, planes1);
		cv::Mat kernelMag;
		cv::magnitude(planes1[0], planes1[1], kernelMag);
		kernelMag += cv::Scalar::all(1);
		cv::log(kernelMag, kernelMag);
		cv::normalize(kernelMag, kernelMag, 0, 1, CV_MINMAX);
		imshow("Kernel Magnitude", kernelMag);


		cv::Mat planes2[2];
		cv::split(inputFFT, planes2);
		cv::Mat imageMag;
		cv::magnitude(planes2[0], planes2[1], imageMag);
		imageMag += cv::Scalar::all(1);
		cv::log(imageMag, imageMag);
		cv::normalize(imageMag, imageMag, 0, 1, CV_MINMAX);
		imshow("Image Magnitude", imageMag);


	}
	


	// Now we do the convolution by visiting each pixel, and
	// computing the Wiener Deconvolution function
	cv::Mat responseFFT(inputFFT.size(), CV_64FC2);

	for( int i = 0; i < inputFFT.rows; i++ )
	{
		for( int  j = 0; j < inputFFT.cols; j++ )
		{
			std::complex<double> H = kernelFFT.at<std::complex<double> >( i, j );
			std::complex<double> I = inputFFT.at<std::complex<double> >( i, j );

			double Su = noiseSignalRatio;
			double Sx = 1;

			std::complex<double> denominator = std::norm( H ) + ( Su / ( Sx - Su ) );
			std::complex<double> value(0,0);
			
			// check the denominator is above an approximation of 0
			if( std::abs( denominator )  > 1.0e-4 )
			{
				value = I * (std::conj( H ) / denominator);
			}
			responseFFT.at<std::complex<double> >(i ,j) = value;
		}
	}




	// Now we take the inverse of the response to the deconvolution
	cv::Mat outputUncropped;
	cv::idft(responseFFT, outputUncropped, cv::DFT_INVERSE + cv::DFT_REAL_OUTPUT+ cv::DFT_SCALE, input.rows);

	// normalise the output to be within the uchar range
	cv::normalize(outputUncropped, outputUncropped, 0, 255, CV_MINMAX);
	
	// cast the output to uchar type
	cv::Mat temp = cv::Mat_<uchar>(outputUncropped);

	// initialise the output and copy the response into it
	output = cv::Mat::zeros(input.size(), input.type());
	temp(cv::Rect(0,0,input.cols, input.rows)).copyTo(output);
}
