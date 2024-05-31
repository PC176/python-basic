# a duck typing is a type of dynamic typing
# it follows following pharse-
# "if a birds look like a duck , swim like a duck , quacks like a duck than its a duck"
# methods is more important than a class for ant object
class pycharm:
    def execute(self):
        print("compiling...")
        print("runing...")


class MyEditor:
    def execute(self):
        print("compiling...")
        print("runing...")
        print("complete")


class code:
    def laptop(self, ide):
        ide.execute()


ide = pycharm()
c1 = code()
c1.laptop(ide)
print("----------------")
ide = MyEditor()
c1.laptop(ide)
