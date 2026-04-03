import random
class FruitQuiz:
    def __init__ (self):
        self.fruits = {"apple": "red", 
                       "banana": "yellow", 
                       "grape": "purple", 
                       "orange": "orange", 
                       "kiwi": "brown"}
    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            print ("What color is {}".format(fruit))
            user_answer = input()
            if user_answer.lower() == color:
                print ("Correct!")
            else:
                print ("Wrong! The correct answer is {}".format(color))
            option = int(input("Do you want to continue? (0 for yes, 1 for no)"))
            if (option):
                break
print ("Welcome to the Fruit Quiz!")
quiz = FruitQuiz()
quiz.quiz()
