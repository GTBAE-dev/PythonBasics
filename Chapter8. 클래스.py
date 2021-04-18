''' 8-1. 클래스 '''
# 클래스 : 연관된 변수와 함수의 집합, 하나의 틀
class alpha_1 : # alphabet 이라는 클래스 생성
    def __init__(self, lowfirst, num_1) : # init(생성자 함수)을 통한 멤버변수 정의(self는 멤버변수 아님)
        self.lowfirst =lowfirst # self.A = A : 클래스 내 정의된 변수 초기화
        self.num_1 = num_1
        print(self.lowfirst, self.num_1)
AA = alpha_1("aA", 1) # AA는 alphabet 클래스의 instance
BB = alpha_1("bB", 2)
