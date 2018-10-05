#!/usr/bin/env python3


from socket import socket
from sys import argv
from select import select

SELECT_TIMEOUT = 0
BUFFER_SIZE = 1024

# with 'BS'. Uses UDP only.
class BSHandler(Handler):
    def __init__(self, peer_addrinfo):
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind(peer_addrinfo)
    def sendRGR(self):
        raise NotImplementedError
    def sendUAR(self):
        raise NotImplementedError
    def sendLSF(self):
        raise NotImplementedError
    def sendLSU(self):
        raise NotImplementedError
    def sendDLB(self):
        raise NotImplementedError
    def parse(self):
        raise NotImplementedError
    def idle(self):
        raise NotImplementedError
    def handle(self):
        raise NotImplementedError
