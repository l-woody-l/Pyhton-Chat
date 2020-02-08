import socket
import sys
from _thread import start_new_thread

HOST = '' #all availabe interfaces
PORT = 3419 #arbitrary non privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[-] Socket Created")

# bind socket
s.bind((HOST, PORT))
print("[-] Socket Bound to port " + str(PORT))
s.listen(10)
print("Listening...")

def Listen_thread(conn):
    conn.send(bytes("Welcome to the Server. Type messages and press enter to send.\n",'utf-8'))

    while True:
        reply = bytes("OK . . ",'ascii') + data
        conn.sendall(reply)
    conn.close()

def Send_thread(conn):

    while True:
        data = conn.recv(1024)
        reply = bytes("OK . . ",'ascii') + data
        conn.send(reply)
    conn.close()

while True:
    conn, addr = s.accept()
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))
    data = str(conn.recv(1024), "utf-8")

    if data == "1":
        print("[-] Connected to ListeningClient")
        start_new_thread(Listen_thread, (conn,))
    if data == "0":
        print("[-] Connected to SendingClient")
        start_new_thread(Send_thread, (conn,))

s.close()