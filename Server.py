import socket

s = socket.socket()
host = 'localhost'
port = 3149

s.bind((host, port))
s.listen(5)
print((host, port))

while True:
    c, addr = s.accept()
    print('got connection from', addr)
    c.send(bytes("Message has been received", 'utf-8'))
    c.close()
