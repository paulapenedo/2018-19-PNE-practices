import socket

# server IP and PORT
PORT = 8086
IP = "192.168.1.36"

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the server
s.connect((IP, PORT))

# close the socket
s.close()

