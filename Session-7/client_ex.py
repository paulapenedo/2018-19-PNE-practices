#Programming our first client

import socket

#Create a socket for communicating woth the server
while True:
    chat = input("What do you want to send? ")
    if chat == "end":
        break
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socket created")

    PORT = 8080
    IP = "212.128.253.64"

    #Connect to the server
    s.connect((IP, PORT))

    s.send(str.encode("HELLO FROM MY CLIENT")) #convert a string in a

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER")
    print(msg)

    break

    s.close()

    print("The end")