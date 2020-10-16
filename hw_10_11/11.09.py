class Dog:

    def __init__(self, name: str = 'Mikki', master: str = 'Viachaslau', age: int = 5):
        self.name = name
        self.age = age
        self.master = master

    def bark(self):
        print(f'Dog {self.name} Woof!')

    def jump(self):
        print(f'Dog {self.name} Jump!')

    def run(self):
        print(f'Dog {self.name} Run!')

    def birthday(self, age):
        self.age = age + 1

    def dog_sleep(self):
        print(f'Dog {self.name} sleep!')


dog = Dog()


class Cat:

    def __init__(self, name: str = 'Margo', master: str = 'Viachaslau', age: int = 6):
        self.name = name
        self.age = age
        self.master = master

    def meow(self):
        print(f'Cat {self.name} Meow.')

    def jump(self):
        print(f'Cat {self.name} Jump!')

    def run(self):
        print(f'Cat {self.name} Run!')

    def birthday(self, age):
        self.age = age + 1

    def cat_sleep(self):
        print(f'Cat {self.name} sleep!')


cat = Cat()


class Parrot:
    def __init__(self, name: str = 'Kesha', master: str = 'Viachaslau', age: int = 10):
        self.name = name
        self.age = age
        self.master = master

    def jump(self):
        print(f'parrot {self.name} Jump!')

    def run(self):
        print(f'parrot {self.name} Run!')

    def birthday(self, age):
        self.age = age + 1

    def parrot_sleep(self):
        print(f'parrot {self.name} sleep!')

    def fly(self):
        print(f'parrot {self.name} fly!')


parrot = Parrot()
parrot.fly()
