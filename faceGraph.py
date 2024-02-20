## 그래프로 시각화하기
import cv2
import pandas as pd
import matplotlib.pyplot as plt

print("시각화 시작!")

# 동영상 읽어오기
mov = cv2.VideoCapture("mov/mov01.avi")
fps = mov.get(cv2.CAP_PROP_FPS)  # fps 불러오기

# hog 선언
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

num = 0

list_df01 = []
list_df02 = []

while(mov.isOpened()):
    ret, frame = mov.read()
    if ret:
        if (num%10==0):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # human, r = hog.detectMultiScale(gray)
            human, r = hog.detectMultiScale(gray, 0, (8, 8), (32, 32), 1.05, 5)
            if (len(human)>0):
                for (x, y, w, h) in human:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255,255,255), 3)
            tmp_se = pd.Series([num/fps,len(human)])
            # tmp_se2 = pd.DataFrame(tmp_se, index=list_df.columns)
            list_df01.append(tmp_se[0])  # 시간
            list_df02.append(tmp_se[1])  # 사람
            # list_df = list_df.append( tmp_se, ignore_index=True )
            # list_df2 = pd.concat([list_df, tmp_se], ignore_index=True)
            # print(list_df2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else:
        break
    num = num + 1

df = pd.DataFrame({'time':list_df01, 'people':list_df02})


mov.release()
cv2.destroyAllWindows()
print("분석 끝!")

plt.plot(df['time'], df['people'])
plt.xlabel('time(sec)')
plt.ylabel('population')
plt.ylim(0, 15)
plt.show()