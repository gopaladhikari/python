f = open("test.txt")

print(f is iter(f))

# for line in f:
#     print(line)

# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

myList = [1, 4, 6, 5]

print(myList is iter(myList))

I = iter(myList)

# print(I)

for i in I:
    print(I.__next__())


D = {"a": 1, "b": 2}

for key in D.keys():
    print(key)

DIter = iter(D)

print(next(DIter))

# R = range(5)

# print(next(R))
