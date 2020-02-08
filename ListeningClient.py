import socket

s = socket.socket()
host = 'localhost'
port = 3419

s.connect((host, port))

s.send(bytes("1", 'utf-8'))

while True:
    print(str(s.recv(1024), "utf-8"))

s.close()