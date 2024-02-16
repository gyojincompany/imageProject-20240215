import cv2  # opencv-python 패키지 설치

img01 = cv2.imread("img/img01.jpg")  # 이미지 불러와서 img01에 저장
height, width = img01.shape[:2]
# img01에 포함된 이미지정보를 shape로 추출->가로,세로 크기만 추출 [0:2]

print(f"이미지의 세로 : {height}")
print(f"이미지의 가로 : {width}")

cv2.namedWindow("sample image", cv2.WINDOW_NORMAL)  # 윈도우 사이즈 조절
cv2.imshow("sample image", img01)  # 이미지 출력하기
cv2.waitKey(0)  # 이미지 표시시간(밀리세컨드단위)->0으로 지정하면 윈도우를 닫을 때까지 표시됨
cv2.destroyAllWindows()  # 윈도우 닫기