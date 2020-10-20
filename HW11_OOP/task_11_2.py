class Car:
    def __init__(self, brand, model, year_of_car_manufacture, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year_of_car_manufacture = year_of_car_manufacture
        self.__speed = speed

    def up_speed(self):
        return self.__speed + 5

    def slow_down_speed(self):
        return self.__speed - 5

    def get_stop_speed(self):
        return self.__speed

    def set_stop_speed(self):
        self.__speed = 0

    def show_speed(self):
        print(self.__speed)


car = Car(brand='Bentley', model='continental', year_of_car_manufacture=2016)
