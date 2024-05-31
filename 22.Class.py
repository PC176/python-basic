#class is blueprint/design of any program
#variable - instance , static/class
#methods - instance , static , class
class computer:
    company = "asus"               #static/class variable
    def __init__(self,proc,ram):   #instance variable
        self.proc = proc
        self.ram = ram
    def display(self):  #instance method - accessor and mutator
        print("processor of computer is ",self.proc,"\n","Ram of computer is ",self.ram)
    @classmethod
    def info(cls):   #class method
        return cls.company
    @staticmethod
    def end():
        return print("End")
c1=computer("i5_6th","4gb")
c2=computer("Ryzon 5","8gb")
c1.display()
c2.display()
print(computer.info())
computer.end()


