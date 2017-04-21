
class Car():

    def __init__(self, car_type, car_model, car_name):
        self.num_of_wheels = 4
        self.speed = 0
        if car_name is None:
            self.car_name = 'General'
        if car_model is None:
            self.car_model = 'GM'


    def drive(self, speed):
        car = Car('MAN', 'Truck', 'trailer')
        self.speed = speed
        return car

