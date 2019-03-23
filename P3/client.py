import socket

# Server IP and PORT
PORT = 8087
IP = "192.168.56.1"

while True:
    msg = ""
    line = ""
    while True:
        line = str(input('> '))
        if line == 'x':
            break
        msg = msg + '\n' + line

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establish the connection to the server(IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the server's response
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()


