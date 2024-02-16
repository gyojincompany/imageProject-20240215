## 동영상 불러오기

import cv2

mov01 = cv2.VideoCapture("mov/mov01.avi")  # 동영상 불러오기
mov01_width = mov01.get(cv2.CAP_PROP_FRAME_WIDTH)  # 동영상의 가로 크기 정보 추출
mov01_height = mov01.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 동영상의 가로 크기 정보 추출
mov01_fps = mov01.get(cv2.CAP_PROP_FPS)  # 동영상 FPS(초당 프레임 수)
mov01_frame_count = mov01.get(cv2.CAP_PROP_FRAME_COUNT)  # 총 프레임 수 추출

print(f"동영상의 가로 크기 : {mov01_width}")
print(f"동영상의 세로 크기 : {mov01_height}")
print(f"동영상의 FPS : {mov01_fps}")
print(f"동영상의 총 프레임 수 : {mov01_frame_count}")

while(mov01.isOpened()):
    ret, frame = mov01.read()  # mov01에 저장된 동영상을 프레임마다 처리하여 불러옴
    # ret->동영상을 잘 불러왔는지 체크하는 bool 변수-> 에러가 없으면 True
    if ret:  # ret 값이 true일때만 동영상 출력
        cv2.imshow("mov01 frame", frame)
        # frame에 저장된 모든 이미지들이 화면에 출력됨
    if cv2.waitKey(1) & 0xFF == ord("q"):  # 키보드의 'q'키가 클릭되면 종료
        break

mov01.release()        
cv2.destroyAllWindows()  # 창 닫기

