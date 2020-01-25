import socket

s = socket.socket()
host = 'localhost'
port = 3149
names = ""

s.bind((host, port))
s.listen(5)
print("Listening")

while True:
    c, addr = s.accept()
    print('got connection from', addr)
    names += str(c.recv(1024), "utf-8")
    c.send(bytes("Connection Established. Recent Names: " + names, "utf-8"))
    print('Connection ended with', addr)
    c.close()