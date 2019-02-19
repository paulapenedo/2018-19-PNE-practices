import socket

PORT = 8080
IP = "212.128.253.64"
MAX_OPEN_REQUEST = 5

#Create a socket for connectign to the client
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.socket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))




while True:
    print("Waiting for connection at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # ...Process the client request
    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    clientsocket.close()
    