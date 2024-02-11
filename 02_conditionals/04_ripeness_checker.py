color = input("Enter the color : ")
ripeness = ""

if color == "Green":
    ripeness = "Unripe"
elif color == "Yellow":
    ripeness = "Ripe"
elif color == "Brown":
    ripeness = "Overripe"
else:
    ripeness = "Invalid Color"

print(ripeness)
