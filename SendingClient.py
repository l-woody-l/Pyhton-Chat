import socket

s = socket.socket()
host = 'localhost'
port = 3419
name = ""

s.connect((host, port))

s.send(bytes("0", 'utf-8'))

while name != "q":
    name = input("Enter something: ")
    s.send(bytes(name, 'utf-8'))

s.close()