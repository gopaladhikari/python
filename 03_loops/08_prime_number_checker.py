number = int(input("Enter the number : "))
count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")
