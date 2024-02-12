string = input("Enter the string : ")

for char in string:
    if string.count(char) == 1:
        print(char)
        break
