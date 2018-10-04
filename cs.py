#!/usr/bin/env python3

from socket import socket
from sys import argv
from time import sleep
from select import select

SELECT_TIMEOUT = 1
BUFFER_SIZE = 1024

# with 'user'
class UserHandler:
   def __init__(self, socket, peer_addr):
        self.socket = socket
        self.peer_addr = peer_addr
    def sendAUR():
        return NotImplemented
    def sendDLR():
        return NotImplemented
    def sendBKR():
        return NotImplemented
    def sendRSR():
        return NotImplemented
    def sendLDR():
        return NotImplemented
    def sendLFD():
        return NotImplemented
    def sendDDR():
        return NotImplemented
    def parse():
        return NotImplemented

# with 'BS'. Uses UDP only.
class BSHandler:
    def __init__(self, socket, peer_addr):
        self.socket = socket
        self.peer_addr = peer_addr
    def sendRGR():
        return NotImplemented
    def sendUAR():
        return NotImplemented
    def sendLSF():
        return NotImplemented
    def sendLSU():
        return NotImplemented
    def sendDLB():
        return NotImplemented
    def parse():
        return NotImplemented
    def handle():
        return NotImplemented

class Waiter:
    def setupTCP(self, port):
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)
        self.tcp_socket.bind((gethostname(), port))
        self.tcp_socket.listen(20)

    def setupUDP(self, port):
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.udp_socket.bind((gethostname(), port))

    def __init__(self, port):
        self.setupUDP()
        self.setupTCP()

    def UDPhandle(self): # XXX
        addrinfo = self.udp_socket.recvfrom(0)[1]
        handler = BSHandler(
        self.setupUDP()

    def TCPhandle(self):
        comm_socket, addrinfo = self.tcp_socket.accept()
        handler = UserHandler(comm_socket, addr_info)
        handler.start()
        self.setupTCP() 

    def service_loop(self):
        while 1:
            ready = select([self.tcp_socket, self.udp_socket], [], [], SELECT_TIMEOUT)[0]
            if self.tcp_socket in ready:
                self.TCPhandle()
            if self.udp_socket in ready:
                self.UDPhandle()

    def start(self):
        self.service_loop()

def main():
    if '-p' in argv:
        port = argv[index('-p') + 1]
    else:
        port = 58056 
    print('Using port', port)
    waiter = Waiter(port)
    waiter.start()
 
if __name__ == '__main__':
    main()
