import logging

logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):  # outer function with arguments as func
    def log_func(*args):  # inner function with any number of arguments.
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args)
        )
        print(func(*args))

    return log_func


def add(x, y):  # func with args
    return x + y


def sub(x, y):  # func with args
    return x - y


add_logger = logger(add)  # assigning outer function to variable
sub_logger = logger(sub)  # assigning outer function to variable

add_logger(3, 3)    # closure
add_logger(4, 5)    # closure

sub_logger(10, 5)   # closure
sub_logger(20, 10)  # closure
