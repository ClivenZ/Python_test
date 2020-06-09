import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow("out")
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow("out", frame)
    if cv2.waitkey(1) == ord('q'):
        break
print("cap is not opened")
cap.release()
cv2.destoyAllwindows()