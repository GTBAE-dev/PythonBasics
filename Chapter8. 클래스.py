''' 8-1. 클래스 '''
# 클래스 : 연관된 변수와 함수의 집합, 하나의 틀
class alpha_1 : # alphabet 이라는 클래스 생성
    def __init__(self, lowfirst, num_1) : # init(생성자 함수)을 통한 멤버변수 정의(self는 멤버변수 아님)
        self.lowfirst =lowfirst # self.A = A : 클래스 내 정의된 변수 초기화
        self.num_1 = num_1
        print(self.lowfirst, self.num_1)
AA = alpha_1("aA", 1) # AA는 alphabet 클래스의 instance
BB = alpha_1("bB", 2)

''' 8-2. 메소드 '''
# 메소드 : 클래스 내의 함수
class alpha_2 : 
    def __init__(self, upfirst, num_2) : 
        self.upfirst = upfirst
        self.num_2 = num_2
        print(self.upfirst, self.num_2)
    def multiple(self, num_def) : # 함수 및 전달값 정의 방법
        if num_def > 1 : 
            for i in range(1, num_def + 1) : 
                print(self.upfirst * i)
        else : 
            for i in range(0, self.num_2) : 
                print(self.upfirst * self.num_2)
                self.num_2 -= 1
CC = alpha_2("Cc", 3)
CC.multiple(4) # 변수.함수() : 클래스 내 함수 사용 방법
CC.multiple(0)