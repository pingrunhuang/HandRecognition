
#include <iostream>

#include "MyLib.cpp"


int main(int argc, const char * argv[]) {
//    init::open_camera();
    cv::String imgDirectory = "/Users/Frank/dev/HandRecognition/Dataset/Set1/0000/0000/frame-0000.jpg";
    // the second parameter can be set to be BGR, GRAYSCALE etc. which are located in Enum of cv::ImreadModes
    cv::Mat img = cv::imread(imgDirectory, cv::IMREAD_UNCHANGED);
    cv::Mat out;
    if (img.empty()) return -1;
    // the second parameter is used to set the size of the window which can be one inside Enum of cv::ImreadModes
    cv::namedWindow("example",cv::WINDOW_AUTOSIZE);
//    DetermineROI(img, out);
    
    cv::imshow("example", out);
    cv::waitKey(0);
    cv::destroyWindow("example");

    return 0;
}
