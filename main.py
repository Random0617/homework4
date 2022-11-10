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

#Part 1
a1 = Animal(4, 6)
a2 = Dog(4, 6)
print(str(a1.width) + " " + str(a1.height))
print(str(a2.width) + " " + str(a2.height))

#Part 2
class Cat(Animal):
    def __init__(self):
        print("Constructing cat")
    def cout(self):
        print("This is a cat")

a1 = Dog()
a2 = Cat()
Animal.cout(a2)
a2.cout()
print(str(issubclass(Cat, Animal))) #True, Cat is a subclass of Animal
print(str(issubclass(Animal, Cat))) #False, Animal is not a subclass of Animal
print(str(isinstance(a1, Animal))) #True, a1 is a Dog, which is an Animal
print(str(isinstance(a1, Dog))) #True, a1 is a Dog
print(str(isinstance(a1, Cat))) #False, a1 is not a Cat
