from vehicle import Vehicle

class Car(Vehicle):

    def brag():
        print('look how cool my car is!')


car1 = Car()
car1.drive()
car1.add_warning('First warning')
print(car1.__dict__)
print(car1)

car2 = Car(200)
car2.drive()
