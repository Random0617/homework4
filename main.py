class Animal():
    def __init__(self, aWidth = 0, aHeight = 0):
        print("Constructing animal")
        self.width = aWidth
        self.height = aHeight
    def cout(self):
        print("This is an animal")

class Dog(Animal):
    def __init__(self, aWidth = 0, aHeight = 0):
        print("Constructing dog")
        self.width = aWidth * 2
        self.height = aHeight * 2
    def cout(self):
        print("This is a dog")

class Cat(Animal):
    def __init__(self):
        print("Constructing cat")
    def cout(self):
        print("This is a cat")

#Part 1
a3 = Animal(4, 6)
a4 = Dog(4, 6)
print(str(a3.width) + " " + str(a3.height)) #4, 6
print(str(a4.width) + " " + str(a4.height)) #6, 12 (used Dog)

a1 = Dog()
a2 = Cat() #cout of Cat by default
Animal.cout(a2) #cout of Animal instead of Cat
a2.cout()

#Part 2
print(str(issubclass(Cat, Animal))) #True, Cat is a subclass of Animal
print(str(issubclass(Animal, Cat))) #False, Animal is not a subclass of Animal
print(str(isinstance(a1, Animal))) #True, a1 is a Dog, which is an Animal
print(str(isinstance(a1, Dog))) #True, a1 is a Dog
print(str(isinstance(a1, Cat))) #False, a1 is not a Cat
