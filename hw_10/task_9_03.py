def my_decorator(func):
    def wrapper(number):
        odd_numbers = 0
        for i in number:
            if i % 2 != 0:
                new_list = odd_numbers + i
                print(new_list)
    return wrapper


@my_decorator
def some_list(x):
    return list(x)


some_list([1, 2, 3, 5, 7])

