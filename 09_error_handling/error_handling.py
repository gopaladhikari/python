fwrite = open("test1.txt", "w")


try:
    fwrite.write("Hello")
finally:
    fwrite.close()


with open("test.txt", "w") as file:
    file.write("Write using with")


print(fwrite)
