def my_decorator(func):
    def wrapper(*args):
        func(*args[::-1])

    return wrapper


@my_decorator
def some_func(*args):
    print(*args)


some_func(1995, 2001, 'hello', 'Slava')