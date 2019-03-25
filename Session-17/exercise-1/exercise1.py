import json
import termcolor

# -- Open the json file
f = open("person_ex1.json", 'r')

# Read the data from the file
# Now person is a dictionary with all the information
person = json.load(f)

print("Total people in the database:",len(person["Persons"]))
people_list = person["Persons"]
for j, person in enumerate(people_list):



    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])

    termcolor.cprint("Age: ", 'green', end="")
    print(person['Age'])

    phoneNumbers = person['PhoneNumber']

    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone{}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("      Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("      Number: ", 'red', end='')
        print(num['number'])
