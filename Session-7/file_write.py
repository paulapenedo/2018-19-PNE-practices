# Example of reading a file located in our local filesystem

FILENAME = "mynotes.txt"

#open the file
f = open(NAME, 'r')

# read the contents of the file
contents = f.read()


print("File opened:  {}".format(f.name))
print("{}".format(contents))

# close the file
f.close()


# now open the file again for adding
f = open(FILENAME, "a")

# write some information to the file
f.write("THIS IS A TEXT EXAMPLE FOR ADDING TO MY FILE")

# close the file again
f.close()

print("The end")