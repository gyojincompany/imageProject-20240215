## 동영상을 이미지로 나누어 저장

import cv2

cap = cv2.VideoCapture("mov/mov01.avi")

num = 0
while(cap.isOpened()):
     ret, frame = cap.read()

     if ret:
         cv2.imshow("mov01 frame", frame)
         filepath = f"snapshot/snapshot_{num}.jpg"
         cv2.imwrite(filepath, frame)
         if cv2.waitKey(1) & 0xFF == ord('q'):
             break

     num = num + 1

cap.release()
cv2.destroyAllWindows()
