import time
from PIL import ImageGrab

time.sleep(5) # 5초 대기: 사용자가 준비하는 시간

# 2초 간격으로 10개
for i in range(1, 11):
    img = ImageGrab.grab() # screenshot 찍어서 저장
    img.save("image{}.png".format(i)) # 파일로 저장
    time.sleep(2)