import socket

s = socket.socket()
host = 'localhost'
port = 3419
message = ""

s.connect((host, port))
s.send(bytes("sender", 'utf-8'))

while message != "q":
    message = input("Enter something: ")
    s.send(bytes(message, 'utf-8'))

s.close()