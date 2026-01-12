print("Select your ride :")
print("1. Bike")
print("2. Car")
choice = input("Enter your choice (1 or 2): ")

if choice==1:
    print("What type of bike do you want?")
    print("a. Mountain Bike")
    print("b. Road Bike")
    choice2=int(input("Enter your choice (a or b): "))
    if choice2=='a':
        print("You have selected Mountain Bike.")
    else:
        print("You have selected Road Bike.")

elif choice==2:
    print("What type of car do you want?")
    print("a. Sedan")
    print("b. SUV")
    choice2=int(input("Enter your choice (a or b): "))
    if choice2=='a':
        print("You have selected Sedan.")
    else:
        print("You have selected SUV.")
else:
    print("Invalid choice. Please select 1 or 2.")
    