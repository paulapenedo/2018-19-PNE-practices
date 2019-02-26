# Example of reading a file located in our local filesystem

NAME = "mynotes.txt"

# open the file
myfile = open(NAME, 'r')

# --my file is an object, let's see what is inside
# print the filename
print("File opened:  {}".format(myfile.name))

# read the whole file into a string
contents = myfile.read()

print("The file contents are: {}".format(contents))
print("The end!")

# close the file
myfile.close()

# my file is an object, and it contains inside many methods and properties