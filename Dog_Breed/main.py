class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

adult_dog = Dog("Buddy", 5)
puppy = Dog("Charlie", 1)
print("Adult Dog Name:", adult_dog.name)
print("Adult Dog Age:", adult_dog.age, "years") 
print("Puppy Name:", puppy.name)
print("Puppy Age:", puppy.age, "years")