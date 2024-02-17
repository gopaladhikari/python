def debug(fn):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"" for key, value in kwargs.items())
        print(f"calling {fn.__name__} with args {args_value} and kwargs {kwargs_value}")
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} returned {result}")
        return result

    return wrapper


@debug
def hello():
    print("Hello")


@debug
def greet(name="Gopal"):
    print("Hello " + name)


hello()
greet("Gopal Adhikari")
