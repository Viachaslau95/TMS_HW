import time


def my_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Lead time: {end-start} seconds.')
    return wrapper()


@my_decorator
def hello():
    name = input('Enter your name: ')
    print(f'Hello my dear friend, {name.title()}!!!')





