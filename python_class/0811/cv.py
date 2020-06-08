import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow("out")
while(True):
    ret, frame = cap.read()
    cv2.imshow("out", frame)
    if cv2.waitkey(30) == ord('q'):
        break
cap.release()
cv2.destoyAllwindows()