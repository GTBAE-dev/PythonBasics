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

