from random import*
class length_cal : 
    def __init__(self) : 
        pass
    def how_long(self, num) : 
        A = "A" * randint(1, 10)
        print("length of A is {0}".format(A))
        print(A * num)
