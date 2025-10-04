# inheritance
# super/parent/base class

class Animal:
    def __init__(self,animal_name):
        self.animal_name = animal_name

    def animal_info(self):
        print(f"Animal name is {self.animal_name}")


# child /derived / child class
        
class Dog(Animal):
    def bark(self):
        print("Woof Woof")

dog = Animal("Puppy")

dog.animal_info()

buddy = Dog("Buddy")

buddy.animal_info()
buddy.bark()


# constructor overriding
# if we write constructor on both classes, the parent constructor will be no longer available to the child class because we are overriding it.
class Parent():
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height= height

        print("Parent Constructor")
        print(f"Name: {self.name} age: {self.age} height: {self.height}")



class Child(Parent):
    def __init__(self, name):
        self.name = name
        print("Child Constructor")
        print(f"Name: {self.name}")

rohan = Child("Rohan")

# super method is used to call parent class constructor to the child class 

class Vehicle:
    def __init__(self,wheels,color):
        self.wheels = wheels
        self.color = color
        print("Parent Constructor!")

class Car(Vehicle):
    def __init__(self, wheels, color,brand):
        super().__init__(wheels, color)
        self.brand = brand
        print("Child COnstructor!")
    def print_detail(self):
        print(f"I have {self.brand} Car. It has {self.wheels} and its color is {self.color}")

car = Car(4,"red","Toyota")
car.print_detail()
