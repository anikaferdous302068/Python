class Myclass:
    __privateVar=27;
    print("I'm inside Myclass")
    def hello(self):
        print("Private variable value: ",self.__privateVar)
foo=Myclass()
foo.hello()