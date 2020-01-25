import socket

s = socket.socket()
host = 'localhost'
port = 3149

s.connect((host, port))
print(s.recv(1024))

name = input("What's your name?")
s.send(name.encode())

s.close()