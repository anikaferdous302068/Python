from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Dog(Animal):
    def move(self):
        print("I can run on all fours.")
class Bird(Animal):
    def move(self):
        print("I can fly in the sky.")
class Fish(Animal):
    def move(self):
        print("I can swim in the water.")
class Snake(Animal):
    def move(self):
        print("I can slither on the ground.")
R = Dog()
R.move()
K = Bird()
K.move()
R = Fish()
R.move()
K = Snake()
K.move()