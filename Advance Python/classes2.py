# static varriables
# static varriable blongs to class instead of intance of class

class Car:
    # static varribale
    num_cars = 0

    def __init__(self,brand,modal):
        self.brand = brand
        self.modal = modal
        Car.num_cars +=1


car1 = Car("Toyata","Camry")
car2 = Car("Honda","Accord")

print(f"Number of cars {Car.num_cars}")