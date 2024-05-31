# List=[2,3,4,5]
# it = iter(List)
# print(it.__next__())
# print(it.__next__())
# print(next(it))
# for i in List:
#     print(i)
#i need my own object
class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
       if self.num<=10:
        val = self.num
        self.num+=1
        return val
       else:
           raise StopIteration
o1=topten()
i = o1.__next__()
print(i)
i = o1.__next__()
print(i)
for i in o1:
    print(i)


