import http.client
import json
import termcolor

PORT = 8005
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)

print("CONTENT: ")


# -- Open the json file
f = open("person.json", 'r')

# Read the data from the file
# Now person is a dictionary with all the information
persons = json.load(f)

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
