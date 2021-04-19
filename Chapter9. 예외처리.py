''' 9-1. 에러 및 예외처리 '''
# 예외처리 : 에러 발생 시, 예외처리 명령문을 통해 명령 프로그램 계속 실행
from random import *
# try : # try : 실행명령문 / except 에러 종류 : 예외 처리 명령문 으로 구성
a = 5
b = [5, "a", 0]
for i in range(0, 4) : 
    try : 
        print(int(a) / int(b[i]))
    except ValueError : # 실행문에 맞지 않는 value 일때 발생하는 오류
        print("not the right value")
    except ZeroDivisionError : # 0 으로 나눴을 때 발생하는 에러
        print("divided by zero")
    except Exception : # 리스트에 값이 없을 때
        print("not in the list")
    except : # 이외의 오류에 대한 처리
        print("what's the error")

