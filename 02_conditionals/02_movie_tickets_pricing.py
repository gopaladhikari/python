age = int(input("Enter your age: "))
day = input("Enter the day of the week: ")

# method 1
print("--------------")

if age < 18:
    if day == "wed":
        print("$6")
    else:
        print("$8")
else:
    if day == "wed":
        print("$10")
    else:
        print("$12")

# method 2
print("--------------")

price = 12 if age >= 18 else 8

if day == "wed":
    price -= 2

print(price)
