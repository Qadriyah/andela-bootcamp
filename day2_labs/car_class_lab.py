class Car():

    def __init__(self, name='General', model='GM', car_type='saloon'):
        self.car_type = car_type
        self.model = model
        self.name = name
        self.speed = 0
        self.num_of_doors = 4
        self.num_of_wheels = 4

        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2

        if self.car_type == 'trailer':
            self.num_of_wheels = 8

    def is_saloon(self):
        if self.car_type == 'saloon':
            return True
        else:
            return False

    def drive(self, gear):
        if self.car_type == 'trailer':
            self.speed = gear * 11
            return self
        else:
            self.speed = 10**gear
            return self


