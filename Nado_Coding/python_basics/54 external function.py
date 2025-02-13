# 직접 import를 해와서 써야하는 함수
# 구글에 list of python modules 를 검색 -> 모듈 목록 열람 가능, 설명과 예제 포함
# glob : 경로 내의 폴더 / 파일 목록 조회 (os 내의 dir 같은 느낌)

import glob
# 확장자가 py인 모든 파일을 알려주는 것
print(glob.glob("*.py"))

# os : os에서 제공하는 기본 기능

import os
# 현재 디렉토리 표시
print(os.getcwd())

folder = "sample_dir"

# sample_dir이라는 폴더가 있으면
if os.path.exists(folder):
    print("folder already exists")
    # 폴더 삭제
    os.rmdir(folder)
    print(folder, "folder has been deleted")

else: 
    # 폴더 생성
    os.makedirs(folder)
    print(folder, "folder has been created")

# glob 이랑 비슷한 효과
print(os.listdir())

# time : 시간 관련

import time
print(time.localtime())
print(time.strftime("%Y-%m-%D %H:%M:%S"))

import datetime
print("today's date is ", datetime.date.today())
# timedelta 두 날짜 사이 간격

today = datetime.date.today()
td = datetime.timedelta(days=100) # 오늘 날짜로 부터 100일 뒤
print("100 days from now is", today + td)