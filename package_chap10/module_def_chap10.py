# Calculator_advanced_module
def power(a, b) :
    print("a = {0}, b = {1}, a ** b = {2}". format(a, b, a**b))
def share(a, b) : 
    try : 
        print("a = {0}, b = {1}, a // b = {2}". format(a, b, a//b))
    except ZeroDivisionError as err : 
        print(err)
def remain(a, b) : 
    try : 
        print("a = {0}, b = {1}, a ","%"," b = {2}". format(a, b, a%b))
    except ZeroDivisionError as err :
        print(err)
# 모듈 직접 실행시 실행 명령문
if __name__ == "__main__" : 
    print("activated in module")
else : 
    print("activated out module")
