#Example of reading a file located in our local filesystem

NAME = "mynotes.txt"

#open the file
myfile = open(NAME, 'r')

print("File opened:  {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))

myfile.close()


f = open(NAME, 'a')
f.write("THIS IS A TEXT EXAMLE FOR ADDING TO MY FILE")
f.close()

print("The end")