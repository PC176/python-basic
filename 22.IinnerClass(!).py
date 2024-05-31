# we can creat a class inside a class
class student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.laptop("i5 7th", 8)

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class laptop:
        def __init__(self, cpu, ram):
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.cpu, self.ram)


s1 = student("Pratik", 1)
s2 = student("Shubham", 2)
s1.show()
s2.show()
l3 = student.laptop("i5 7th", 8)
l1 = s1.lap
l2 = s2.lap
print(str(l1))
print(str(l2))
print(l3)
print(id(l1))
print(id(l2))
print(id(l3))
