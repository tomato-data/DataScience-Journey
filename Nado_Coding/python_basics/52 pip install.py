# python 에서는 새로운 코드를 다 작성하는 것 보다 
# 이미 만들어진 코드를 적재적소에 사용하는 게 중요한 능력
# 이미 검증받아진 패키지를 받아 씀으로서 안정적이게 사용가능

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip list를 커맨드창에 쓰면 설치 되어있는 패키지를 볼 수 있음
# pip show --- 라고 치면 그 패키지에 대한 정보를 알려줌 
# pip install --upgrade --- = 업데이트
# pip uninstall --- = 삭제