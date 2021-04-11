''' 1-1. 숫자 자료형 '''
# 정수(음, 양), 실수(소수) 모두 출력 가능
print(10)
print(-10)
print(3.14)
# 사칙연산 가능
print(10+10)
print(10-10)
print(10*10)
print(10/10)

''' 1-2. 문자열 자료형 '''
# 문자열은 작은 따옴표 또는 큰 따옴표로 감싸줘야함
print('Hello World')
print("Hello World")
# 문자열 곱셈 가능(이외의 사직연산은 불가)
print("Hello World"*3)

''' 1-3. Boolean 자료형 '''
# True / False 을 출력하는 문자열
print(0<1)
print(0>1)
print(0<=1) # 등호(=)는 부등호 오른쪽에 위치해야함(print(0=<1)는 오류)
print(True)
print(False) # 시작 문자가 대문자여야 Boolean 으로 인식
print(not True) # not 은 반대로 출력

''' 1-4. 변수 '''
# 변수 : 값을 저장하는 공간
animal = "소"
print(type(animal)) #변수의 자료형 출력 
age = 4
print(type(age))
is_adult = age >= 3
print(type(is_adult))
# +를 사용하여 합칠 시 str 자료형만 출력 가능, 다른 자료형은 str으로 바꿔주어야함 
print(animal + "는 " + str(age) + "살이면 어른일까?" + str(is_adult)) # 다른 자료형으로 바꾸는 방법: str()
print(animal, "는", age, "살이면 어른일까?", is_adult) # , 를 사용하여 합칠 시 모든 자료형 출력 가능