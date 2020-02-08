import socket

s = socket.socket()
host = 'localhost'
port = 3419

s.connect((host, port))

name = input("What's your name? ")
s.send(bytes(name, 'utf-8'))

s.close()