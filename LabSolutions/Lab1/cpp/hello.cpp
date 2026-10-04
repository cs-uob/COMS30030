/////////////////////////////////////////////////////////////////////////////
//
// COMS30121 - hello.cpp
// TOPIC: create, save and display an image
//
// Getting-Started-File for OpenCV
// University of Bristol
//
/////////////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <opencv/cv.h>        //you may need to
#include <opencv/highgui.h>   //adjust import locations
#include <opencv/cxcore.h>    //depending on your machine setup

using namespace cv;

int main() {
  
  //create a black 256x256, 8bit, gray scale image in a matrix container
  Mat image(256, 256, CV_8UC1, Scalar(0));
  
  //draw white text HelloOpenCV!
  putText(image, "HelloOpenCV!", Point(70, 70),
		FONT_HERSHEY_COMPLEX_SMALL, 0.8, cvScalar(255), 1, CV_AA);

  //save image to file
  imwrite("myimage.jpg", image);

  //construct a window for image display
  namedWindow("Display window", CV_WINDOW_AUTOSIZE);

  //visualise the loaded image in the window
  imshow("Display window", image);

  //wait for a key press until returning from the program
  waitKey(0);

  //free memory occupied by image 
  image.release();

  return 0;
}