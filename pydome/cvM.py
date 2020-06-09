from __future__ import print_function
import cv2 as cv
import argparse
#BS MOG2
backSub = cv.createBackgroundSubtractorMOG2()
#capture open
capture = cv.VideoCapture(0)
if not capture.isOpened:
    print("cap is not opened!")
    exit(0)

kernel1 = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
kernel2 = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
while True:
    ret, frame = capture.read()
    if frame is None:
        break
    
    fgMask = backSub.apply(frame)
    cv.morphologyEx(fgMask, cv.MORPH_OPEN, kernel1)
    #location

    cv.dilate(fgMask, kernel2)
    cv.rectangle(frame, (3, 8), (100,20), (0,0,255), -1)
    

    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)

    if cv.waitKey(100) or ord('q'):
        break
capture.release()
cv.destroyAllWindows()