## 이미지 속의 사람 얼굴 검출하기

import cv2

# 검출 준비
cascade_file = "haarcascade_frontalface_alt.xml"  # 앞을 보는 얼굴 찾기 모델
cascade = cv2.CascadeClassifier(cascade_file)

# 검출
img02 = cv2.imread("img/img02.jpg")  # 이미지 불러오기
gray = cv2.cvtColor(img02, cv2.COLOR_BGR2GRAY)  # 흑백이미지로 변경
face_list = cascade.detectMultiScale(gray, minSize=(50, 50))  # 얼굴들 검출

for (x, y, w, h) in face_list:
    cv2.rectangle(img02, (x, y), (x+w, y+h), (0, 0, 255), thickness=3)  #BGR색상값 참고
# 이미지 속 사람의 얼굴 리스트에서 x,y좌표와 얼굴의 가로크기, 세로크기를 추출하여 사각형으로 표시

cv2.namedWindow("face search", cv2.WINDOW_AUTOSIZE)
cv2.imshow("face search", img02)
cv2.imwrite("face.jpg", img02)
cv2.waitKey(0)
cv2.destroyAllWindows()




