#!/usr/bin/python3

import socket
import sys

HOSTNAME = "localhost"
PORT = 58011
BUFFER_SIZE = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_adress = (HOSTNAME, PORT)
print('TCP server starting on {} port {}'.format(*server_adress))

sock.bind(server_adress)  # binding the socket to the specified port

sock.listen(2)  # allowing the server to receive connections and specifying how many accepted until new are refused

while True:
    # waiting connection
    print('waiting for a connection')
    connection, client_adress = sock.accept()  # accepted client connection
    try:
        print('client connected: ', client_adress)

        # now do stuff
        # as example it will receive the data in small chunks and then send it back

        while True:
            data = connection.recv(BUFFER_SIZE)
            print('received {!r}'.format(data))

            if data:
                print('sending data back')
                connection.sendall(data)
            else:
                print('no data received from', client_adress)
                break

    finally:
        #Cleaning up
        connection.close()
