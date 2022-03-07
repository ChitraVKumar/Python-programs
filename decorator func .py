# Decorator functions

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print("Display ran here")


@decorator_function
def display_info(name, age):
    print("Display_info ran args ({},{})".format(name, age))


display()
display_info('chitra', 29)
