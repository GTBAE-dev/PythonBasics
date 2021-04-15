''' 6-1. 함수 '''
# 함수 : 특정 역할을 하는 식
def function_print(): # 함수를 정의하는 방법
    print("This is how fuctions ACT") # 함수가 호출되었을 때 실행문
function_print()

''' 6-2. 전달값 & 반환값 '''
# 전달값 : 함수에 입력되어 처리되는 값 / 반환값 : 함수 처리의 결과 값
def function_calculate(A, B) : # 함수 내의 전달값 전달하는 법
    if A > 0 and B > 0 : # 조건에 따라 다른 결과 출력 가능
        return A + B, A - B # return 으로 반환값을 함수의 결과로 받음
    elif A < 0 and B < 0 : 
        return A * B, A / B # 여러 개의 반환값 받기 가능
    else :
        return A, B
result_1, result_2 = function_calculate(3, 4)
print("Result of function_calculate is {0} and {1}.".format(result_1, result_2))

''' 6-3. 기본값 & 키워드값 '''
# 기본값 : 전달값 미설정시 기본으로 전달값으로 설정되는 값
def function_basic(a = "AA", b = "BB", num = 10) : # 전달값에 기본값을 설정하는 방법
    print("a is [{0}], b is [{1}] and num is [{2}]".format(a, b, num))
function_basic("CC", "DD", 100)
function_basic() # 전달값 설정 X : 기본값 출력 방법
# 키워드값 : 함수 호출시 값 뿐만 아니라 변수명까지 지정해서 전달하는 방법
function_basic(a = "CC", b = "DD", num = 100) # 변수명과 함께 전달값 지정
function_basic(num = 100, a = "CC", b = "DD") # 순서가 바뀌어도 변수명에 따라 지정됨

''' 6-4. 가변인자 '''
# 가변인자 : 함수의 전달값을 여러개 설정하는 방법
def function_variable(*c) : # *을 붙여 가변인자로 설정
    C = 1
    for i in c : # 가변인자는 튜플형태로 저장
        print("c_{0} is {1}    ".format(i, C), end = "")
        C += 1    
function_variable(10, 20, 30, 40, 50) # 전달값 변수 내 여러 객체 저장
print("")

''' 6-5. 지역변수 & 전역변수 '''
# 지역변수 : 함수 내에서만 쓸 수 있는 변수
# 전역변수 : 프로그램 내 어디서든 호출되는 변수
parameter = 100 # 전역변수
def function_last_1(num) : 
    parameter = 10 # 지역변수 : 동일한 변수명 사용시 함수 내에서는 지역변수 사용
    return parameter - num
print("Result of function_last_1 is {0}".format(function_last_1(5)))
print(parameter) # 함수 외부에서는 전역변수 호출
def function_last_2(num) : 
    global parameter # 전역변수를 함수로 호출하는 방법 1
    return parameter - num
print("Result of function_last_2 is {0}".format(function_last_2(30)))
def function_last_3(parameter, num) : # 전역변수를 함수로 호출하는 방법 2
    return parameter - num
print("Result of function_last_3 is {0}".format(function_last_3(parameter, 10)))
print("Result of function_last_3 is {0}".format(function_last_3(20, 10))) # 전달값 설정 시, 전역변수 무시
# 전역변수를 많이 설정하는 것은 프로그램이 복잡해져 권장하지 않음