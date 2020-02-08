import socket

s = socket.socket() #192.168.1.160
host = 'localhost'
port = 3419

s.connect((host, port))

name = input("What's your name? ")
s.send(bytes(name, 'utf-8'))
print(str(s.recv(1024), "utf-8"))
print(str(s.recv(1024), "utf-8"))
s.send(bytes(name, "utf-8"))

s.close()