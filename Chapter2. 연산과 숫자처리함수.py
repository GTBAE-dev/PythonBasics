''' 2-1. 사칙연산 '''
# 계산 결과를 출력
print(4+4)
print(4-4)
print(4*4)
print(4/4)
print((4+4)*4) #우선 순위 연산 가능
print(4**4) # a**b ; a의 b제곱
print(5//4) # a//b ; a나누기 b의 몫
print(5%4) # a%b ; a나누기 b의 나머지
# 변수 연산
number = 4
print(number)
number += 4 # number = number + 4 와 동일
print(number)
number -= 4 # number = number - 4 와 동일
print(number)
number /= 4 # number = number / 4 와 동일
print(number)
number *= 4 # number = number * 4 와 동일
print(number)
number **= 4 # number = number ** 4 와 동일
print(number)
number //= 4 # number = number // 4 와 동일
print(number)
number %= 4 # number = number % 4 와 동일
print(number)

''' 2-2. 비교연산 '''
# True / False 를 출력
print(5>4)
print(5>=4) # 등호는 부등호 뒤에 위치해야함
print(5<4)
print(5<=4)
print(4==4) # a==b ; a와 b가 같은면 True
print(4!=4) # a!=b ; a와 b가 같지 않으면 True
print(not(4==4)) # not 사용시 반대로 출력
print((4>0) and (5>0)) # A and B ; A와 B 모두 True 여야 True
print((4>0) & (5>0)) # & = and
print((4>0) or (4>5)) # A or B ; A와 B 중 하나만 True면 True
print((4>0) | (4>5)) # |(shift+\) = or
print(5>4>6) # 이중비교

''' 2-3. 숫자처리함수 '''
print(abs(-4)) # abs(a) ; a의 절대값
print(pow(4,3)) # pow(a,b) ; a^b
print(max(4,3)) # max(a,b) ; a와 b 중 최대값
print(min(4,3)) # min(a,b) ; a와 b 중 최소값
print(round(4.51)) # round(a) ; a의 반올림 값
# math library 활용
from math import *
print(floor(4.99)) # floor(a) ; a의 내림 값
print(ceil(4.01)) # floor(a) ; a의 올림 값
print(sqrt(16)) # sqrt(a) ; a의 제곱근
# random library 활용
from random import *
print(random()) # 0.0 ~ 1.0 미만 임의 값 생성
print(random()*10) # 0.0 ~ 10.0 미만 임의 값 생성
print(int(random()*10)) # 0 ~ 10 미만 임의 값 생성(정수처리)
print(int(random()*10+1)) # 1 ~ 10 이하 임의 값 생성
print(randrange(1,10)) # randrange(a,b) ; a 이상 b 미만 임의 정수 값 생성
print(randint(1,10)) # randint(a,b) ; a 이상 b 이하 임의 정수 값 생성