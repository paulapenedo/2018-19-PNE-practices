import socket

# configure the server's IP and PORT
PORT = 8085
IP = "192.168.1.36"
MAX_OPEN_REQUEST = 5

# Create a socket for connecting to the client
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN:REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))


while True:
    # accept connections from outside
    # the server is waiting for connections
    print("Waiting for connection at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # this server do nothing. The new socket is closed
    clientsocket.close()