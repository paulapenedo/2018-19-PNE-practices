import socket

PORT = 8080
IP = "212.128.253.64"

#create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((IP, PORT))

s.close()