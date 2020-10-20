class Computer:
    def __init__(self, name: str, model: int, price: int, weight: int):
        self.__name = name
        self.__model = model
        self.__weight = weight
        self.price = price

    def not_in_stock(self):
        print(f'{self.__name}({self.__model}) not in stock!')

    def sale(self):
        print(self.price - 100)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight


class Bar:
    def __init__(self, name: str, number_of_seats: int, average_check: int, comment: str):
        self.__name = name
        self.__number_of_seats = number_of_seats
        self.__average_check = average_check
        self.comment = comment

    def closed(self):
        print(f'Bar {self.__name} closed!')

    def up_check(self):
        print(self.__average_check + 7)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def number_of_seats(self):
        return self.__number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, number_of_seats):
        self.__number_of_seats = number_of_seats

    @property
    def average_check(self):
        return self.__average_check

    @average_check.setter
    def average_check(self, average_check):
        self.__average_check = average_check


class Hotel:
    def __init__(self, name: str, number_of_rooms: int, price: int):
        self.__name = name
        self.__number_of_rooms = number_of_rooms
        self.__price = price

    def no_free_rooms(self):
        print(f'In Hotel {self.__name} no free rooms!')

    def closed_some_room(self):
        print(self.__number_of_rooms - 10)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def number_of_rooms(self):
        return self.__number_of_rooms

    @number_of_rooms.setter
    def number_of_rooms(self, number_of_rooms):
        self.__number_of_rooms = number_of_rooms

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


class Cinema:
    def __init__(self, name: str, number_of_halls: int, price: int, comment: str):
        self.__name = name
        self.__number_of_halls = number_of_halls
        self.__price = price
        self.comment = comment

    def no_tickets(self):
        print(f'In {self.__name} no tickets, sorry.')

    def closed_hall(self):
        print('Hall number 3 is closed for renovation.')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def number_of_halls(self):
        return self.__number_of_halls

    @number_of_halls.setter
    def number_of_halls(self, number_of_halls):
        self.__number_of_halls = number_of_halls

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


class COVID19:
    def __init__(self, cases_of_illness: float, recovered: float, lethal_outcomes: float):
        self.__cases_of_illness = cases_of_illness
        self.__recovered = recovered
        self.__lethal_outcomes = lethal_outcomes\


    @property
    def cases_of_illness(self):
        return self.__cases_of_illness

    @cases_of_illness.setter
    def cases_of_illness(self, cases_of_illness):
        self.__cases_of_illness = cases_of_illness

    @property
    def recovered(self):
        return self.__recovered

    @recovered.setter
    def recovered(self, recovered):
        self.__recovered = recovered

    @property
    def lethal_outcomes(self):
        return self.__lethal_outcomes

    @lethal_outcomes.setter
    def lethal_outcomes(self, lethal_outcomes):
        self.__lethal_outcomes = lethal_outcomes


comp = Computer(name='Lenovo', model=340, price=1900, weight=1800)
comp.not_in_stock()
comp.sale()
bar = Bar(name='Lidbeer', number_of_seats=150, average_check=40, comment='nice bar')
bar.closed()
bar.up_check()
hotel = Hotel(name='Radison', number_of_rooms=50, price=300)
hotel.no_free_rooms()
hotel.closed_some_room()
cinema = Cinema(name='Silver Screen', number_of_halls=7, price=20, comment='Good Cinema')
cinema.no_tickets()
cinema.closed_hall()
korona = COVID19(cases_of_illness=40.6, recovered=27.8, lethal_outcomes=1.12)
