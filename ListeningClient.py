import socket

s = socket.socket()
host = 'localhost'
port = 3419

s.connect((host, port))

while True:
    print(str(s.recv(1024), "utf-8"))

s.close()