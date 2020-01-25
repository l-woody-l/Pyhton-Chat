import socket

s = socket.socket()
host = 'localhost'
port = 3149

s.connect((host, port))

name = input("What's your qadojajskd: ")
s.send(bytes(name, 'utf-8'))
print(str(s.recv(1024), "utf-8"))

s.close()