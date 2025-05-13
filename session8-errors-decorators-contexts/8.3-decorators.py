import time

def do_nothing_decorator(func):  # func is the function being decorated
    def wrapped(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapped


def remember(func):  # func is the function being decorated
    cached_value = None

    def wrapped():
        nonlocal cached_value   # nonlocal is necessary for basic datatypes. (it works with lists and dicts...)
        if cached_value is not None:
            return cached_value
        else:
            cached_value = func()
            return cached_value
    return wrapped

@remember
def m1():
    return time.time()

print (m1())
print (m1())
time.sleep(2)
print (m1())
print (m1())
