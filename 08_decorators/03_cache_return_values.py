import time


def cache_return_values(fn):
    cache_values = {}
    print(cache_values)

    def wrapper(*args):
        if args in cache_values:
            return cache_values[args]

        result = fn(*args)
        cache_values[args] = result
        print(cache_values)
        return result

    return wrapper


@cache_return_values
def long_running(a, b):
    time.sleep(3)
    return


print(long_running(1, 2))
print(long_running(1, 2))
print(long_running(4, 2))
