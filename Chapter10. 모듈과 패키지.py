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
