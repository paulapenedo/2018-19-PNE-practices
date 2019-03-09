import socket
import termcolor
import sys


# esta es mi IP
IP = " 192.168.56.1"
PORT = 8088

msg = input("> ")

# Now we can create the socket and connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to teh server
s.connect((IP, PORT))

# send the request message to the server
s.send(str.encode(msg))


# receive the response from the server
response = s.recv(2048).decode()

# print the response
print("Response: {}".format(response))

s.close()