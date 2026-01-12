medical_cause= input("Did you have a medical cause Y or N?")
atten= int(input("Enter your attendance : "))
if medical_cause == 'Y':
    print("You are allowed")
else:
    if atten >= 75:
        print ("You are allowed")
    else: 
        print ("You are not allowed")
        

