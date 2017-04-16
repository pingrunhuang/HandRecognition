# Hand gesture recognition application

This application is developped with XCode Version 8.3


### How to set up library dependency of opencv 3 in XCode?
In the build setting part, enter the following value:
'''
HEADER_SEARCH_PATHS:"/usr/local/include"

Library Search Path:"/usr/local/lib"

Other Linker Flag:"-lopencv_calib3d -lopencv_core -lopencv_features2d -lopencv_flann -lopencv_highgui -lopencv_imgcodecs -lopencv_imgproc -lopencv_ml -lopencv_objdetect -lopencv_photo -lopencv_shape -lopencv_stitching -lopencv_superres -lopencv_ts -lopencv_video -lopencv_videoio -lopencv_videostab"
'''

### Dataset
The training dataset is ["Sebastien Marcel Static Hand Posture Database"](http://www.idiap.ch/resource/gestures/)
The training image is in ppm(portable pixmap) format with 70 to 90 pixels
