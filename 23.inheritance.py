#inheritance - using a feature of existing class
#single , multilevel , multiple
#1.single level inheritance
class A:
    def feature1(self):
        print("feature1")
    def feature2(self):
        print("feature2")
class B(A):
    def feature3(self):
        print("feature3")
    def feature4(self):
        print("feature4")
a=A()
b=B()
a.feature1()
a.feature2()
b.feature3()
b.feature4()
#after = B(A)
b.feature1()
b.feature2()
print("---------------------------------------------------------")
#2.multilevel
class A:
    def feature1(self):
        print("feature1")
    def feature2(self):
        print("feature2")
class B(A):
    def feature3(self):
        print("feature3")
    def feature4(self):
        print("feature4")
class C(B):
    def feature5(self):
        print("feature5")
a=A()
b=B()
c=C()
a.feature1()
a.feature2()
b.feature3()
b.feature4()
b.feature1()
b.feature2()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
print("-------------------------------------------")
#3.multiple
class A:
    def feature1(self):
        print("feature1")
    def feature2(self):
        print("feature2")
class B:
    def feature3(self):
        print("feature3")
    def feature4(self):
        print("feature4")
class C(A,B):
    def feature5(self):
        print("feature5")
a.feature1()
a.feature2()
b.feature3()
b.feature4()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()