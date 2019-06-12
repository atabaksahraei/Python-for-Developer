def write(text):
    with open("myFile.txt", "w") as file:
        file.write(text)

def append(text):
    with open("myFile.txt", "a") as file:
        file.write(text)

def readDirty():
    file = open("myFile.txt", "r")
    content = file.readlines()
    file.close()
    return content  

def read():
    with open("myFile.txt", "r") as file:
        for l in file:
            yield l

def printFile():
    with open("myFile.txt", "r") as file:
        for line in file:
            print(line.strip())

write("ABC\n")
append("CDE\n")
append("EFG\n")

names = [".NEt", "VSCode", ".NET Core"]
for name in names:
    append(name)
    append("\n")

print(read())

printFile()
