from logger import get_logger

logger = get_logger()


def my_decorator(func):
    dict_args = dict()

    def save_args(*args):
        logger.debug(f'Argument={args}, dict_args={dict_args}')
        if args not in dict_args:
            dict_args[args] = func(*args)
        return dict_args[args]

    return save_args


@ my_decorator
def some_func(a, b):
    logger.debug(f'вызов функции с аргументами: {a}, {b}')
    return a + b


my_decorator(some_func(2, 5))
my_decorator(some_func(3, 5))
my_decorator(some_func(2, 5))
my_decorator(some_func(4, 6))
