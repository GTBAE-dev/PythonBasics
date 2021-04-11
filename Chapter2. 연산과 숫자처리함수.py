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

