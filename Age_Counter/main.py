try:
    age=int(input("Enter your age: "))
    print("Your age is:", age)
    if age%2==0:
        print("Your age is even.")
    else:
        print("Your age is odd.")
except ValueError as ex:
    print("Please enter a valid integer for age.")

