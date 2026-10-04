/////////////////////////////////////////////////////////////////////////////
//
// COMS30121 - RGBtoGRAY.cpp
//
// University of Bristol
//
/////////////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <opencv/cv.h>        //you may need to
#include <opencv/highgui.h>   //adjust import locations
#include <opencv/cxcore.h>    //depending on your machine setup

using namespace cv;

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
 imwrite( "gray.jpg", gray_image );

 return 0;
}
