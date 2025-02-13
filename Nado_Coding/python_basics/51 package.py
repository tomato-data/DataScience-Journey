# 하나의 디렉토리에 여러 모듈을 가져다 놓은 것 = 패키지

# import travel.Thailand 
# # . 뒤에 맨 뒷 부분은 모듈이나 패키지만 가능, 클래스나 함수는 불가능
# # from import 구문으로는 사용 가능

# trip_to = travel.Thailand.ThailandPackage()
# trip_to.detail()

# from travel.Thailand import ThailandPackage

# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import Vietnam

# trip_to = Vietnam.VietnamPackage()
# trip_to.detail()
 
# from random import * 처럼

from travel import *
# # 별을 쓴다는거는 travel 안에 모든 것을 가져온다는 뜻
# # 실제로는 개발자가 문법 상에서 공개범위를 설정 해줘야함
# # 패키지에 포함된 것 중에서 import 되기를 원하는 것만 공개, 아닌 것은 비공개 설정 가능


# trip_to = Vietnam.VietnamPackage()
# trip_to.detail()
# trip_to2 = Thailand.ThailandPackage()
# trip_to2.detail()

#  패키지, 모듈 위치확인

import inspect
import random

# random 모듈의 파일위치를 알려줌
print(inspect.getfile(random))
print(inspect.getfile(Thailand))

# 만든 모듈을 /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10
# 폴더에 넣으면 언제든 사용 가능