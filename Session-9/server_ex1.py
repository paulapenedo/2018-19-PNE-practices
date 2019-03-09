import socket
import termcolor
import sys

PORT = 8088
IP = "192.168.56.1"
MAX_OPEN_REQUEST = 5


# the function is in charge of servicing the client
def process_client(cs):
    """Process the client request.
    Parameters: cs:socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")
    termcolor.cprint(msg, 'blue')
    if msg == "EXIT":
        sys.exit(0)

    # print the received message, for debugging
    print("Message from the client: {}". format(msg))

    # send the message back to the client, because we are the server
    cs.send(str.encode(msg))

    # close the socket
    cs.close()

# MAIN PROGRAM

# Create a socket for connecting to the client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# bind the socket to the IP and PORT
s.bind((IP, PORT))

# configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
s.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(s))


while True:
    # accept connections from outside
    # the server is waiting for connections
    print("Waiting for connection at: {}, {}".format(IP, PORT))
    (clientsocket, address) = s.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # service the client
    process_client(clientsocket)
