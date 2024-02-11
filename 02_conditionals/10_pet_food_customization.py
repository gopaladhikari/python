pet_age = int(input("Enter the pet age : "))
pet_specy = input("Enter the pet specy : ")


if pet_specy == "dog" and pet_age < 2:
    print("Puppy food")

elif pet_specy == "cat" and pet_age > 5:
    print("Senior cat food")
else:
    print("General pet food")
