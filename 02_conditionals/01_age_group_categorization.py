age = int(input("Enter your age: "))

if age < 13:
    print("Children")
elif age < 20:
    print("Teenagers")
elif age < 60:
    print("Adults")
else:
    print("Senior")
