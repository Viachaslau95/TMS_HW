class Car:
    def __init__(self, brand, model, year_of_car_manufacture, speed: int = 0):
        self.__brand = brand
        self.__model = model
        self.__year_of_car_manufacture = year_of_car_manufacture
        self.__speed = speed

    def up_speed(self, km: int = 5):
        self.__speed += km
        return self.__speed

    def slow_down_speed(self, km: int = 5):
        self.__speed -= km
        return self.__speed

    def get_stop_speed(self):
        return self.__speed

    def set_stop_speed(self):
        self.__speed = 0

    def upend_speed(self):
        self.__speed = -self.__speed
        return self.__speed

    def show_speed(self):
        print(self.__speed)


car = Car(brand='Bentley', model='continental', year_of_car_manufacture=2016)



