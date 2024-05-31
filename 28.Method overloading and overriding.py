#in python there is no method overloading - but we can implement it by if else
#method overloading means same name different no of parameters
#method overriding meang same name and same no of paremeters
# method overloading-
class sum:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s=a

        return s
    # def __str__(self):
    #     return "{} {}".format(self.n1,self.n2,)
a1=sum(4,5)
print(a1.add(2,3,6))
print(a1.add(2,3))
print(a1.add(2))

# print(a1.__str__())
#overriding
class A:
    def show(self):
        print("In A class")
class B(A):
    def show(self):
        print("In B class")
a1=B()
a1.show()



