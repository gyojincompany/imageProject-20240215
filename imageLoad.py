import cv2  # pip install opencv-python

img = cv2.imread("img/img01.jpg")
height, width = img.shape[:2] # img에 포함된 이미지 정보를 shape로 추출하여 가로 세로 크기 추출
print("이미지 가로: " + str(width))
print("이미지 세로: " + str(height))
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.imshow("img",img) # 이미지 출력 함수
cv2.waitKey(0) # 이미지 표시 시간 0->윈도우 닫을 때까지 표시됨, 밀리단위
cv2.destroyAllWindows() # 윈도우 닫기