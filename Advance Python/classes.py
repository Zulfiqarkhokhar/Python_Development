 # crearting class

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printMsg(self):
        print(f"Hello My name is {self.name} and I am {self.age} years old")
    # methods
    def talk(self):
        print("My name is Zulfiqar")

# create intance of class

intance = Person("Zulfiqar",27)
intance.talk()
intance.printMsg()


# constructor allow us to define varriable in class

class Car:
    def __init__(self): # constructor function
        self.color="Black"
        self.price = 1200000
    
    def print_specs(self):
        print(f"My Car color is {self.color} and its price is {self.price}")

obj = Car()
obj.print_specs()


