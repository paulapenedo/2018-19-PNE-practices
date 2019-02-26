# Create a client
import socket

from P1.seq import Seq
PORT = 8081
IP = "192.168.1.36"

# create an INET, STREAMING socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect with the server
clientsocket.connect((IP, PORT))

while True:
    message = input("Introduce a sequence: ")
    message = message.upper()

    for letter in message:
        if letter != "A" or letter != "C" or letter != "G" or letter != "T":
            print("This is not a valid sequence.")
            message = input("INtroduce a valid sequence")
        else:
            continue
    seq1 = Seq(message)
    seq2 = seq1.complement()
    seq3 = seq1.reverse()

    msg1 = "The complement sequence of " + seq1 + "is: " + seq2.strbase
    msg2 = "The reverse sequence of " + seq1 + "is: " + seq3.strbase

    # send the message to the server
    clientsocket.send(str.encode(msg1))
    clientsocket.send(str.encode(msg2))

    text = clientsocket.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER: \n")
    print(text)

    clientsocket.close()