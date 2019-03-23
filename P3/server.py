import socket
import termcolor

# Configure the Server's IP and PORT
from P3.Seq import Seq

PORT = 8087
IP = "192.168.56.1"
MAX_OPEN_REQUESTS = 5


def operations(s, command):
    print("Making command", command)
    if command == "len":
        return s.len()
    elif command == "complement":
        return s.complement()
    elif command == "reverse":
        return s.reverse()
    elif command == "countA":
        return s.count('A')
    elif command == "countT":
        return s.count('T')
    elif command == "countG":
        return s.count('G')
    elif command == "countC":
        return s.count('C')
    elif command == "percA":
        return s.perc('A')
    elif command == "percT":
        return s.perc('T')
    elif command == "percG":
        return s.perc('G')
    elif command == "percC":
        return s.perc('C')
    else:
        return "Error"


def valid(s):
    valid_sequence = ['A', 'C', 'G', 'T']
    for letter in s:
        if letter not in valid_sequence:
            return False

    return True


def process_client(cs):
    """Process the client request.
    Parameters: cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")
    termcolor.cprint(msg, 'green')

    print('Msg ', msg)

    lines = msg.split('\n')

    if not msg or msg == "\n":
        response = 'ALIVE'
    else:
        print("Ratting", lines[0])
        if valid(lines[1]):
            response = 'OK\n'
            s = Seq(lines[1])
            for i in range(2, len(lines)):
                print("Command", i, lines[i])
                o = operations(s, lines[i])
                response = response + str(o) + '\n'
        else:
            response = 'ERROR'

     # Print the received message
    print("Request message: {}".format(msg))

    # Send the msg back to the client
    cs.send(str.encode(response))

    # Close the socket
    cs.close()


# MAIN PROGRAM
# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # Accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connection from client: {}".format(address))

    process_client(clientsocket)
