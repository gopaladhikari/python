def evenNumberGenerator(limit):
    li = []
    for i in range(1, limit + 1):
        if i % 2 == 0:
            yield i


for i in evenNumberGenerator(10):
    print(i)
