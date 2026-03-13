class Employee:
    def __init__ (self):
        print ('Employee created')
    def __del__ (self):
        print ("Destructor called")
def Creat_obj():
    print ("Creating Object....")
    obj = Employee()
    print ("Function end....")
    return obj
print ("Calling Create_obj() function....")
obj = Creat_obj()
print ("Program End....")