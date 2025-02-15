from abc import *

class Animal(metaclass = ABCMeta): #2
    @abstractmethod
    def eat(self):
        pass

a = Animal()