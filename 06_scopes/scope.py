username = "Gopal Adhikari"
x = 99


# def print_username():
#     username = "new name"
#     print(username)


# def add(y):
#     return x + y


# result = add(4)
# print(result)


# print(username)
# print_username()


# def func():
#     global username
#     username = "new name 1"
#     print(username)


# func()

# print(username)


# def f1():
#     x = 5
#     print(x)

#     def f2():
#         print(x)

#     return f2


# func = f1()

# print(func())


## closure


def coder(a):
    def actual(x):
        return x**a  # a = 2, x = 3

    return actual


res = coder(2)

print(res(3))
