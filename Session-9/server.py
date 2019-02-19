import socket

PORT = 8080
IP = "212.128.253.64"
MAX_OPEN_REQUEST = 5

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)