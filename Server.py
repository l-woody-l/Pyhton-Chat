import socket

s = socket.socket()
host = 'localhost'
port = 3149

s.bind((host, port))
s.listen(5)
print("Listening")

while True:
    c, addr = s.accept()
    print('got connection from', addr)
    c.send(bytes("Connection Established", 'utf-8'))
    c, name = s.accept()
    ##c.send()
    c.close()
