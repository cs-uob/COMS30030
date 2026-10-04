/////////////////////////////////////////////////////////////////////////////
//
// COMS30121 - draw.cpp
// TOPIC: create, draw and save an image
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

  //create a red 256x256, 8bit, 3channel BGR image in a matrix container
  Mat image(256, 256, CV_8UC3, Scalar(0, 0, 255));

  //put white text HelloOpenCV
  putText(image, "HelloOpenCV", Point(70, 70),
    FONT_HERSHEY_COMPLEX_SMALL, 0.8, cvScalar(255, 255, 255), 1, CV_AA);

  //draw blue line under text
  line(image, Point(74, 90), Point(190, 90), cvScalar(255, 0, 0),2);

  //draw a green smile 
  ellipse(image, Point(130, 180), Size(25,25), 180, 180, 360,     cvScalar(0, 255, 0), 2);
  circle(image, Point(130, 180), 50, cvScalar(0, 255, 0), 2);
  circle(image, Point(110, 160), 5, cvScalar(0, 255, 0), 2);
  circle(image, Point(150, 160), 5, cvScalar(0, 255, 0), 2);

  //save image to file
  imwrite("myimage.jpg", image);

  //free memory occupied by image 
  image.release();

  return 0;
}
