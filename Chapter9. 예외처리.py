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

''' 9-2. 사용자 정의 에러 및 raise & finally '''
# 사용자 정의 에러

class NegativeError(Exception) : # class 에러명(Exception) : 을 통한 사용자 에러 정의
    def __init__(self, msg) : # msg 멤버변수 정의 및 초기화
        self.msg = msg 
    def __str__(self) : # __str__ 메소드를 통해 멤버변수를 반환
        return self.msg # 에러 발생 시 멤버변수를 메소드 통해 반환, 출력
try:
    a = randint(-5, 5)
    b = randint(-5, 5)
    if (a > 0 and b < 0) or (a < 0 and b > 0) :
        raise NegativeError("result is negative") # raise 에러명 : 특정조건에서 에러 발생시키기
    print("{0}/{1}={2:.2f}".format(a, b, (a/b)))
except ZeroDivisionError as err : # err을 통해 에러 메시지 직접 출력 가능
    print("divided by zero")
    print(err)
except NegativeError as err : # 사용자 정의 에러에서는 멤버변수(msg)가 에러메시지
    print("not positive")
    print(err)
finally : # 에러 발생과 상관 없이 무조건 실행되는 명령문
    print("a is {0}, b is {1}".format(a, b))