#!/usr/bin/env python3

from socket import * 
from select import select

class NewHandler:
    def __init__(self, port):
        self.port = port
        self.setupUDP()
        self.setupTCP()
        self.active_handlers = []

    def setupTCP(self):
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)
        self.tcp_socket.setblocking(0)
        self.tcp_socket.bind((gethostname(), self.port))
        self.tcp_socket.listen(20)

    def setupUDP(self):
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.udp_socket.setblocking(0)
        self.udp_socket.bind((gethostname(), self.port))

    def acceptUDP(self):
        addrinfo = self.udp_socket.getpeername()
        handler = BSHandler(addrinfo)
        self.active_handlers += handler
        self.setupUDP()

    def acceptTCP(self):
        comm_socket = self.tcp_socket.accept()[0]
        handler = UserHandler(comm_socket)
        self.active_handlers += handler
        self.setupTCP() 

    def idle(self):
        # this select does not time out.
        ready = select([h.get_socket() for h in self.active_handlers] + [self.tcp_socket, self.udp_socket], [], [])[0]
        if self.tcp_socket in ready:
            self.acceptTCP()
        if self.udp_socket in ready:
            self.acceptUDP()
        for handler in self.active_handlers:
            closed = handler.handle()
            if closed:
                self.active_handlers.remove(handler)
        
    def start(self):
        while 1:
            self.idle()

def main():
    nh = NewHandler(50000)
    nh.start()

if __name__ == '__main__':
    main()
