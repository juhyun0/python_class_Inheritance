class Car:
    def ride(self):
        print("Run")

class FlyingCar(Car):
    def ride(self):
        super().ride()
        print("Fly")

my_car=FlyingCar()
my_car.ride()