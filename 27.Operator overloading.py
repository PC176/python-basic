#we can over load the operator
a=2
b=7
c=int.__add__(
    a,b
)
print(c)
#when we use + then it call __add__ function
class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1 , m2)
        return s3
    def __sub__(self, other):
        if(self.m1<other.m1):
            self.m1, other.m1 = other.m1 , self.m1
            self.m2, other.m2 = other.m2 , self.m2
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        s4 = student(m1 , m2)
        return s4

s1=student(34,43)
s2=student(45,54)

# s3 = s1.m1  s2.m2
# print(s3)
s3 = s1 + s2
print(s3.m2)
print(s3.m1)
s4 = s1 - s2
print(s4.m2)
print(s4.m1)