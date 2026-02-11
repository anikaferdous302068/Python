import random
playing = True
number=random.randint(0,9)
print ("I will generate a number between 0 and 9, and you have to guess the number one digit at a time.")
while playing:
    guess=int(input("Give me your best guess: "))
    if number==guess:
        print("Congratulations! You guessed the number correctly.")
        print("The number was:", number)
        break
    else:
        print("Sorry, that's not correct. Try again!")
        print("The number was:", number)