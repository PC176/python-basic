#python is a procedural , functional and oops programing language
# Class is a design of a program and object is a instance of class
# atributes and behavior is type of object



class student1:
    def marks(self):
        marks1=[12,12,12,12,43]
        print(marks1)
s = student1()
s.marks()
student1.marks(s)
print("-----------Constructor--------------------")
class student:
    def __init__(self,n,r,m,a):
        self.n=n
        self.r=r
        self.m=m
        self.a=a
    def display(self):
        print("Name=",self.n,"\n","Roll=",self.r,"Marks=",self.m ,"Age=",self.a)
s1 = student("Pratik",1,89,19)
s2 = student("Sai",2,38,20)
s1.display()
s2.display()