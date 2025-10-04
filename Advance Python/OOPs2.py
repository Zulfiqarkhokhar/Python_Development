# Polymorphism
# with Method Over Riding

class Animal:
    def make_sound(self):
        print("Generic Sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()


# method OverLoading

# compile time polymorphism or static polymorphism

class MathOperation:
    def add(self,a,b):
        return a+b
    
    def add(self,a,b,c):
        return a+b+c
    
add_nums = MathOperation()
#print(add_nums.add(1,2))
print(add_nums.add(1,2,3))
