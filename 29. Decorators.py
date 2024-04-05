import time


def calc_time(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        finito = time.time()
        print(f"Operation completed in {finito - begin} seconds.")
        return result

    return wrapper


@calc_time
def square(list):
    result = []
    for i in list:
        result.append(i * i)
    return result


@calc_time
def kup(list):
    result = []
    for i in list:
        result.append(i ** 3)
    return result


@calc_time
def add(*args):
    time.sleep(1)
    return sum(args)


print(add(5, 97))
