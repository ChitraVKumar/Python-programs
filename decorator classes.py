# Decorator classes

class decorator_class(object):

    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print("Golds Gym certified trainer details {}".format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)


@decorator_class
def display():
    print("Who is the best trainer in Secunderabad? ")


@decorator_class
def display_info(name, age):
    print("Info about best trainer in Town ({}, {})".format(name, age))


display()
display_info("Edwine", 25)
