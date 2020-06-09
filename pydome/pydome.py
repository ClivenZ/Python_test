import cv2
import argparse

backSub = cv2.BackgroundSubtractorMOG2()
cap = cv2.VideoCapture(0)

#cv2.namedWindow("OUT_PUT")
#cv2.namedWindow("MOG2_PUT")

#kernel1 = cv2.getStructuringElement()
#kernel2 = cv2.getStructuringElement()

while(cap.isOpened()):
    ret, frame = cap.read()  
    fgMask = backSub.apply(frame)
    cv2.rectangle(frame, (10,2), (100,20), (255,255,255), -1)
    cv2.putText(frame, str(cap.get(cv2.CAP_PROP_POS_FRAMES)), (15,15),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    cv2.imshow("OUT_PUT", frame)
    cv2.imshow("MOG2_PUT",fgMask)
    
    Keyboard = cv2.waitkey(30)
    if Keyboard == 'q' or Keyboard == 27 :
        break

cap.release()
cv2.destroyAllWindows()
