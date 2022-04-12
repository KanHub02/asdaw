class Car:
    wheels = 4

    def __init__(self, model, year, color, penalties=0.0):
        self.year = year
        self.model = model
        self.color = color
        self.penalties = penalties

    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')

    def tuning(self, new_color):
        self.color = new_color
#
#
# mazda_car = Car('Mazda RX=7', 2022, 'black', 100.5)
# bmw = Car('BMW M-3', 2019, 'black')
# print(mazda_car)
# print(f'{mazda_car.model}, {mazda_car.color}, {mazda_car.penalties}')
# bmw.drive('Tokyo')
# mazda_car.drive('Biskek')
# mazda_car.tuning(new_color='Green')



class Truck(Car):
    def __init__(self, model, color, penalties, load_capacity):
        Car.__init__(self, model, color, penalties)
        self.load_capacity= load_capacity