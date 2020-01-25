import socket

s = socket.socket()
host = 'localhost'
port = 3149
decoding = "utf-8"

s.bind((host, port))
s.listen(5)
print("Listening")

while True:
    c, addr = s.accept()
    print('got connection from', addr)
    name = (c.recv(1024))
    c.send (bytes("Connection Established, ", decoding) + name)
    c.close()
