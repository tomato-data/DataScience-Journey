# 필요한 부분을 '부품'화 = 모듈화
# 함수정의, 클래스 등의 파이썬 문장 등을 담고있는 파일을 모듈 (확장자 = .py)

# 같은 경로 or python library 들이 모여있는 폴더에 있어야 사용가능

# import theater_module as mv

# mv.price(3)
# mv.morning_price(4)
# mv.soldier_price(5)

# from theater_module import *

# price(3)
# morning_price(4)
# soldier_price(5)

# 원하는것만 따로 빼올 수 있음
# from theater_module import price, morning_price

from theater_module import soldier_price as price

price(3)