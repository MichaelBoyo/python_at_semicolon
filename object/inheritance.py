class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print("i am barking")


class Dog(Animal):
    def __init__(self, name, breed, color="brown"):
        super().__init__(name, breed)
        self.owner = color

    def speak(self):
        print('i am barking myself')

    pass


dog = Dog("aja", "rawt")
print(dog.name)
print(dog.breed)
dog.speak()
