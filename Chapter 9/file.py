# how to create text files using Python
file = open("example.txt", "w")
# w means write mode
file.write("Hello, World! \n This is a sample text file. \nWelcome to Python file handling.")
file.close()

# how to read text files using Python
file = open("example.txt", "r")
content = file.read()
print("File Content: ")
print(content)
file.close()



# readlines example
file = open("example.txt", "r")
lines = file.readlines()
print("File Lines:")
for line in lines:
    print(line.strip())
    # strip() is used to remove leading/trailing whitespace characters
file.close()

# append mode example
file = open("example.txt", "a")
file.write("\nThis line is appended to the file.")
file.close()


# with statement example
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content using with statement:")
    print(content)