//
//  MyLib.cpp
//  HandRecognition
//
//  Created by huangrunping on 04/04/2017.
//  Copyright © 2017 Runping. All rights reserved.
//

#include "MyLib.hpp"

/*
 * part 1: image preprocess
 */
void RGBToYCRCB(cv::InputArray mat, cv::Mat out){
    cvtColor(mat, out, CV_BGR2YCrCb);
}


/*
 * part 2: detection of the ROI
 */

int THRESHOLD = 18;
double Cbmax = 105;
double Cbmin = 80;
double Crmax = 165;
double Crmin = 130;
void DetermineROI(cv::Mat in, cv::Mat out){
    double Cr, Cb, d1, d2, d3, d4;
    for(int i = 0; i < in.cols; i++){
        for(int j = 0; j < in.rows ; j++){
            cv::Vec3f bgrPixel = in.at<cv::Vec3b>(i, j);
            Cr = bgrPixel[1];
            Cb = bgrPixel[2];
            d1 = sqrt(pow(Cb - Cbmin, 2) + pow(Cr - Crmin, 2));
            d2 = sqrt(pow(Cb - Cbmin, 2) + pow(Cr - Crmax, 2));
            d3 = sqrt(pow(Cb - Cbmax, 2) + pow(Cr - Crmin, 2));
            d4 = sqrt(pow(Cb - Cbmax, 2) + pow(Cr - Crmax, 2));
            if ( (d1 + d2 + d3 + d4) <= THRESHOLD ){
                out.at<uchar>(i, j) = 255;// hand region detected
            }
        }
    }
}


/*
 * part 3: Initial window for rendering video captured by camera
 */
int BUILT_IN_CAM = 0;
int EXTERNAL_CAM = 1;

void open_camera(){
    cv::namedWindow( "source" , cv::WINDOW_AUTOSIZE );
    cv::namedWindow( "YCrCb" , cv::WINDOW_AUTOSIZE);
    cv::namedWindow( "ROI" , cv::WINDOW_AUTOSIZE);
    cv::VideoCapture cap;
    cap.open( BUILT_IN_CAM );
    cv::Mat source;
    cv::Mat YCrCb;
    cv::Mat ROI;
    for(;;) {
        cap >> source;
        if( source.empty() ) break;
            cv::imshow( "source" , source );
            RGBToYCRCB(source, YCrCb);
            cv::imshow( "YCrCb" , YCrCb);
            DetermineROI(YCrCb, ROI);
            cv::imshow( "ROI" , ROI);

            // wait for 33ms, if users do not press any button, will continue
            // else, the ASCII code of the button will return
            if( cv::waitKey(33) >= 0 )
                break;
        }
}




