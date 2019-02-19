import socket

# SERVER IP, PORT
IP = "192.168.1.36"
PORT = 8086

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

msg = "Hello"

# Send the request message to the server
s.send(str.encode(msg))

# Receive the servers response
response = s.recv(2048).decode()

# Print the server's response
print("Response: {}".format(response))

s.close()