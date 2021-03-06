import http.client

PORT = 8020
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# Send the request message, using the GET method
conn.request("GET", "/listusers")

# Read the response message from teh server
r1 = conn.getresponse()

# Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# Read the response's body
data1 = r1.read().decode("utf-8")

print("CONTENT: ")

# Print the received data
print(data1)