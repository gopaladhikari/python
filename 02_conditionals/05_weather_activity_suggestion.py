weather = input("Enter the weather : ")
activity = ""

if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"
else:
    activity = "Invalid Weather"

print(activity)
