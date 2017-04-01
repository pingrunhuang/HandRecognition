#ifndef Init_h
#define Init_h
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

namespace init {
    int BUILT_IN_CAM = 0;
    int EXTERNAL_CAM = 1;
    
    void open_camera(){
        cv::namedWindow( "Image window" , cv::WINDOW_AUTOSIZE );
        cv::VideoCapture cap;
        cap.open( init::BUILT_IN_CAM );
        cv::Mat frame;
        for(;;) {
            cap >> frame;
            if( frame.empty() ) break;
            cv::imshow( "Image window" , frame );
            // wait for 33ms, if users do not press any button, will continue
            // else, the ASCII code of the button will return
            if( cv::waitKey(33) >= 0 )
                break;
        }
    }
    
}// init

#endif /* Init_h */
