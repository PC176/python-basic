#python not have defualt abstract but we can use a library to implement this
#Abstract method is method which not have any body and deffination also we can not create a object
# that class which have abstract methods is called abstract class
from abc import ABC , abstractmethod
class comoputer(ABC):
    @abstractmethod
    def process(self):
         pass

class laptop(comoputer):
    def process(self):
        print("Running")
# p1 = comoputer()
p1=laptop()
p1.process()