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

''' 8-3. 상속 '''
# 상속 : 기존 클래스(부모)를 상속하여 다른 클래스(자식) 생성
class alpha_3(alpha_1, alpha_2) : # 하나 이상의 클래스를 상속 가능
    def __init__(self, upfirst, lowfirst, num_1, num_2, all_low) : 
        alpha_1.__init__(self, lowfirst, num_1) # 부모 클래스의 멤버변수 초기화
        alpha_2.__init__(self, upfirst, num_2) # 부모 클래스의 멤버변수를 취사선택하여 상속 불가
        self.all_low = all_low
DD = alpha_3("Dd", "dD", 3, 4, "dd") # 부모 클래스의 init 함수 사용됨
DD.multiple(3) # 부모의 함수 사용 가능

''' 8-4. 연산자 오버로딩 '''
# 연산자 오버로딩 : 부모 클래스에서 정의된 함수를 자식 클래스에서 재정의하여 사용
class alpha_4(alpha_2) : 
    def __init__(self, upfirst, all_up, num_2) : 
        super().__init__(upfirst, num_2) # super을 이용한 멤버변수 초기화 방법(self 없어도 됨, 다중상속에는 사용X)
        self.all_up = all_up
    def multiple(self, num_def) : 
        print(self.upfirst * num_def, "\t", self.all_up * num_def)
EE = alpha_4("Ee", "ee", 5)
EE.multiple(5) # 같은 함수명, 자식 클래스는 자식 함수 적용
