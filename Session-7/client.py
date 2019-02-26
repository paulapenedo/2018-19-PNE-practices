# Programming our first client
import socket

# Create the socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# print some information about the socket
print()
print("Socket created:")
print(s)
print("End")

# we are setting our first connection, so we need to specify the IP address and the port
PORT = 8080
IP = "212.128.253.64"

#Connect to the server
s.connect((IP, PORT))

# send data, no strings.
# it is necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT"))


# receive data from the server
msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER:\n")
print(msg)

s.close()

print("The end")