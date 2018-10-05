#!/usr/bin/env python3

from socket import socket
from select import select

class NewHandler:
    def setupTCP(self, port):
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)
        self.tcp_socket.setblocking(0)
        self.tcp_socket.bind((gethostname(), port))
        self.tcp_socket.listen(20)

    def setupUDP(self, port):
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.udp_socket.setblocking(0)
        self.udp_socket.bind((gethostname(), port))

    def __init__(self, port):
        self.setupUDP()
        self.setupTCP()
        self.active_handlers = None

    def acceptUDP(self):
        addrinfo = self.udp_socket.recvfrom(0)[1] #XXX: may not work.  
        handler = BSHandler(addrinfo)
        self.active_handlers += handler
        self.setupUDP()

    def acceptTCP(self):
        comm_socket = self.tcp_socket.accept()[0]
        handler = UserHandler(comm_socket)
        self.active_handlers += handler
        self.setupTCP() 

    def check_handlers(self):
        # this select does not time out.
        ready = select([self.tcp_socket, self.udp_socket], [], [])[0]
        if self.tcp_socket in ready:
            acceptTCP()
        if self.udp_socket in ready:
            acceptUDP()
        for handler in self.active_handlers:
            if handler.dead:
                active_handlers.remove(handler)
            else:
                handler.check()
        
    def start(self):
        while 1:
            check_handlers()
