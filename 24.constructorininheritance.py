#we can use constructor in inheritance
class A:
    def __init__(self):
        print("in it A")
    def feature1(self):
        print("feature1")
    def feature2(self):
        print("feature2")
class B(A):
    def __init__(self):
        super().__init__()
        print("in it b")
    def feature3(self):
        print("feature3")
    def feature4(self):
        print("feature4")
    def ggg(self):
        super().feature2()
a = B()
a.ggg()
#sub class can access the all feature of super class but super class can not
#when we create a object of sub class then it call init of self if unavailable then call init of super class
#method resolution order = left to right for inheritance calling
