import time


def timer(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f"{fn.__name__} ran in {end_time - start_time} seconds")
        return result

    return wrapper


@timer
def example_function(n):
    time.sleep(n)


example_function(4)
