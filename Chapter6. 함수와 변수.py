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