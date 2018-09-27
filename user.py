#!/usr/bin/python3

import socket
import sys

HOSTNAME = "localhost"
PORT = 58011
BUFFER_SIZE = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCPIP Socket creation

server_adress = (socket.gethostbyname(HOSTNAME), PORT)

print('connecting to server')

sock.connect(server_adress)

try:

    #Sending data
    msg = b'Some message to send'
    print('sending {!r}'.format(msg))
    sock.sendall(msg)

    #Answer lookup
    amount_received = 0
    amount_expected = len(msg) #how long is the message we're gonna receive

    while amount_received < amount_expected:
        data = sock.recv(BUFFER_SIZE)
        amount_received += len(data)
        print('received {!r}'.format(data))


finally:
    print("closing socket")
    sock.close()
