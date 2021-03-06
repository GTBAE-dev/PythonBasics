''' 10-1. 모듈 '''
# 모듈 : 함수, class 등 필요한 것들을 담고 있는 파일(확장자 py)
# 같은 폴더 내에 있어야 사용 가능
import module_chap10 # 모듈 호출 방법 1
module_chap10.plus(3, 5) # 모듈.함수(a, b)로 함수 사용 가능
import module_chap10 as cal # 모듈 호출 방법 2 : cal로 모듈 사용
cal.minus(10, 5)
from module_chap10 import* # 모듈 호출 방법 3 : 해당 모듈에 있는 모든 것 사용
division(10, 5)
from module_chap10 import multiple # 모듈 내 특정 함수 호출
multiple(3, 4)
from module_chap10 import multiple as mul # 모듈 내 특정 함수를 mul 로 사용
mul(5, 2)

''' 10-2. 패키지 '''
# 패키지 : 모듈을 모아놓은 집합(디렉토리, 폴더)
import package_chap10.module_class_chap10 # 패키지 내 모듈 호출, 모듈의 함수나 클래스는 .연결로 호출 불가
short1 = package_chap10.module_class_chap10
short1.length_cal.how_long(3, 1) # 패키지 내 모듈 내 클래스 내 메소드 사용 방법(클래스 와 메소드 같이 쓸 때는 괄호내 self 위치에 임의의 수 필요(3))
from package_chap10.module_class_chap10 import length_cal # 모듈 내 클래스(함수) 호출 방법
short2 = package_chap10.module_class_chap10.length_cal() # 호출 후에는 줄여서 사용 가능
short2.how_long(4) # 패키지 내 모듈 내 클래스 내 함수 사용
# 패키지 공개 범위 설정(__init__.py) : __all__ = [모듈명] 을 통해 공개할 모듈만 설정
from package_chap10 import* # package_chap10 내 모든 걸 가져오겠다는 의미
short3 = module_def_chap10
# 모듈 직접 실행 : if __name__ == "__main__" : 직접실행 명령문 / else : 호출 명령문
short3.remain(3,4) 
short3.power(4,2)

''' 10-3. 패키지 설치 방법 '''
# 많은 패키지가 만들어져 있고, 갖다 쓸 수 있음(google > pypi)
# beautiful soup(for web scrapping)
# 터미널에 pip list : 설치된 pip list
# 터미널에 pip show beaultifulsoup4 : 설치된 beautifulsoup4 에 대한 정보
# 터미널에 pip install --upgrade beautifulsoup4 : 설치된 beautifulsoup4 업그레이드
# 터미널에 pip uninstall beautifulsoup4 : 설치된 beautifulsoup4 삭제
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

''' 10-4. 내장함수 '''
# 내장함수 : 이미 설치되어 있어 import 안하고 사용할 수 있는 함수
# input : 사용자 입력을 받는 함수, str 형태로 값을 받음
# dir : 어떤 객체를 넘겨줬을 때, 그 객체에 어떤 함수를 사용할 수 있는지
import random
print(dir(random))
import pickle
print(dir(pickle))
print(dir())
lst = [1, 2, 3]
print(dir(lst))
sub = "AA"
print(dir(sub))

''' 10-5. 외장함수 '''
# 외장함수 : import를 하여 사용할 수 있는 함수(google > list of python modules)
# inspect : 모듈의 위치를 확인할 수 있는 모듈
import inspect
print(inspect.getfile(random))
print(inspect.getfile(module_chap10))
# glob : 경로 내의 폴더/파일 목록 조회
import glob
print(glob.glob("*.py")) # 확장자 py 인 모든 파일 찾기
# os : 운영체제에서 제공하는 기본 기능들(ex. 폴더를 만들고 삭제)
import os
print(os.getcwd()) # 현재 데렉토리를 표시해달라
folder = "folder"
if os.path.exists(folder): # 해당 이름의 폴더가 있는지
    print("existing folder")
    os.rmdir(folder) # 폴더 삭제
    print(folder, "folder deleted")
else:
    os.makedirs(folder) #해당 이름 폴더 생성
    print(folder, "folder made")
print(os.listdir()) # glob 과 유사한 함수
# time : 시간과 관련된 함수
import time
print(time.localtime()) # 현재 날짜, 시각
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 현재 날짜, 시각
import datetime
today = datetime.date.today() # 현재 날짜
print(today)
td = datetime.timedelta(days=100) # 날짜 100일 차이
print(today + td)