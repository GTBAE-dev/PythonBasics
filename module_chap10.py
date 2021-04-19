# Calculator_module
def plus(a, b) :
    print("a = {0}, b = {1}, a + b = {2}". format(a, b, a+b))
def minus(a, b) : 
    print("a = {0}, b = {1}, a - b = {2}". format(a, b, a-b))
def multiple(a, b) : 
    print("a = {0}, b = {1}, a * b = {2}". format(a, b, a*b))
def division(a, b) : 
    try : 
        print("a = {0}, b = {1}, a / b = {2}". format(a, b, a/b))
    except ZeroDivisionError as err :
        print(err)