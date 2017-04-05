import cv2
import numpy as np
import math

THRESHOLD = 18
Cbmax = 105
Cbmin = 80
Crmax = 165
Crmin = 130
def determineROI(input):
    row = input.shape[0]
    col = input.shape[1]
    output = input
    for i in range(row):
        for j in range(col):
            bgrPixel = input[i,j]
            Cr = bgrPixel[1];
            Cb = bgrPixel[2];
            d1 = math.sqrt(math.pow(Cb - Cbmin, 2) + math.pow(Cr - Crmin, 2));
            d2 = math.sqrt(math.pow(Cb - Cbmin, 2) + math.pow(Cr - Crmax, 2));
            d3 = math.sqrt(math.pow(Cb - Cbmax, 2) + math.pow(Cr - Crmin, 2));
            d4 = math.sqrt(math.pow(Cb - Cbmax, 2) + math.pow(Cr - Crmax, 2));
            if (d1 + d2 + d3 + d4) <= THRESHOLD :
                # hand region detected as black
                output[i,j] = [0,0,0]
            else:
                output[i,j] = [255,255,255]
    return output

BUILT_IN_CAM = 0
EXTERNAL_CAM = 1
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # cv2.imshow( "Source image" , frame)
    YCRCB = cv2.cvtColor( frame, cv2.COLOR_BGR2YCR_CB )
    # cv2.imshow( "Destination image" , YCRCB )
    ROI = determineROI(YCRCB)
    cv2.imshow( "ROI", ROI )
    # wait for 33ms, if users do not press any button, will
    # else, the ASCII code of the button will return
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break
