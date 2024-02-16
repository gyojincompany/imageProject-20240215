## 이미지 속에서 사람 찾기

import cv2

hog = cv2.HOGDescriptor()  # HOG 객체 생성
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())  # 사람인식 인수 넣어주기

img = cv2.imread("img/img01.jpg")  # 샘플 이미지 불러오기
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 이미지를 흑백사진으로 바꾸기

human, r = hog.detectMultiScale(img_gray)  # 이미지에서 사람을 검출

# 이미지에서 검출된 사람에게 사각형 그리기
if len(human)>0:
    for (x, y, w, h) in human:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

cv2.namedWindow("human search", cv2.WINDOW_NORMAL)
cv2.imshow("human search", img)
cv2.imwrite("img/human_search.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
