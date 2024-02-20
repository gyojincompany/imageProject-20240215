## 이미지 속의 사람 얼굴이 어느 방향을 보고 있는 검출하기

# dlib 설치
# pip install cmake 설치 후 dlib-19.24.1-cp311-cp311-win_amd64.whl 설치
# pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
# 단, 파이썬 버전에 맞는 whl 설치되어야 함

import cv2
import dlib
import math

# 검출 준비
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# 얼굴 랜드마크 68개 점 불러오기
detector = dlib.get_frontal_face_detector()  # 정면 얼굴 불러오기

# 이미지에서 검출
img = cv2.imread("img/img02.jpg")
dets = detector(img,1)

for k, d in enumerate(dets):
    shape = predictor(img, d)

    # 얼굴 영역 표시
    color_f = (0, 0, 225)
    color_l_out = (255, 0, 0)
    color_l_in = (0, 255, 0)
    line_w = 3
    circle_r = 3
    fontType = cv2.FONT_HERSHEY_SIMPLEX
    fontSize = 1
    cv2.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()), color_f, line_w)
    cv2.putText(img, str(k), (d.left(), d.top()), fontType, fontSize, color_f, line_w)

    # 중심을 계산할 사각형 준비
    num_of_points_out = 17
    num_of_points_in = shape.num_parts - num_of_points_out
    gx_out = 0
    gy_out = 0
    gx_in = 0
    gy_in = 0
    for shape_point_count in range(shape.num_parts):
        shape_point = shape.part(shape_point_count)
        #print("얼굴 랜드마크No.{} 좌표 위치: ({},{})".format(shape_point_count, shape_point.x, shape_point.y))
        #얼굴 랜드마크마다 그리기
        if shape_point_count<num_of_points_out:
            cv2.circle(img,(shape_point.x, shape_point.y),circle_r,color_l_out, line_w)
            gx_out = gx_out + shape_point.x/num_of_points_out
            gy_out = gy_out + shape_point.y/num_of_points_out
        else:
            cv2.circle(img,(shape_point.x, shape_point.y),circle_r,color_l_in, line_w)
            gx_in = gx_in + shape_point.x/num_of_points_in
            gy_in = gy_in + shape_point.y/num_of_points_in

    # 중심 위치 표시
    cv2.circle(img,(int(gx_out), int(gy_out)),circle_r,(0,0,255), line_w)
    cv2.circle(img,(int(gx_in), int(gy_in)),circle_r,(0,0,0), line_w)

    # 얼굴 방향 계산
    theta = math.asin(2*(gx_in-gx_out)/(d.right()-d.left()))
    radian = theta*180/math.pi
    print("얼굴 방향:{} (각도:{}도)".format(theta,radian))

    # 얼굴 방향 표시
    if radian<0:
        textPrefix = "   left "
    else:
        textPrefix = "   right "
    textShow = textPrefix + str(round(abs(radian),1)) + " deg."
    cv2.putText(img, textShow, (d.left(), d.top()), fontType, fontSize, color_f, line_w)


cv2.namedWindow("frontal face", cv2.WINDOW_AUTOSIZE)
cv2.imshow("frontal face", img)
cv2.imwrite("frontalFace.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



