from abc import ABC, abstractmethod
class AbsClass(ABC):
    def print (self, x):
        print("passed value: ", x)
    @abstractmethod
    def take(self):
        print ("We are inside Absclass task")
class test_class(AbsClass):
    def take(self):
        print ("We are inside test_class task")
test_obj = test_class()
test_obj.take()
test_obj.print(100)
