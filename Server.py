import socket
import sys
from _thread import start_new_thread

senders = []
listeners = []

HOST = ''
PORT = 3419

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[-] Socket Created")

s.bind((HOST, PORT))
print("[-] Socket Bound to port " + str(PORT))
s.listen(5)
print("Listening...")

def check_thread():
    while True:
        if len(senders) > 0:
            msg = str(conn.recv(1024), "utf-8")
            for x in listeners:
                x.send(bytes(msg, 'utf-8'))

while True:
    start_new_thread(check_thread, ())
    while True:
        conn, addr1 = s.accept()
        type = str(conn.recv(1024), "utf-8")
        if type == "listener":
            listeners.append(conn)
        if type == "sender":
            senders.append(conn)
        print("[-] Connected to " + addr1[0] + ":" + str(addr1[1]))
        #Listener.send(bytes("Welcome to the Server. Type messages and press enter to send.\nType \"q\" to disconnect.", 'utf-8'))
        #while True:
            #msg = str(Sender.recv(1024), "utf-8")
            #Listener.send(bytes(msg, 'utf-8'))

s.close()