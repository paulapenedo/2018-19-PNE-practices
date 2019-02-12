#Example of reading a file located in our local filesystem

NAME = "mynotes.txt"

#open the file
myfile = open(NAME, 'r')

print("File opened:  {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))

