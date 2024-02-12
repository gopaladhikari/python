num = int(input("Enter the number : "))

for i in range(1, 1 + num):
    if i == 5:
        continue
    else:
        print(i, "x", num, "=", i * num)
