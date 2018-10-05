#!/usr/bin/env python3

'''
	'addr': IP or hostname.
	'addrinfo': tuple in the form ('addr', port).
'''

from socket import socket
from sys import argv
from time import sleep
from select import select

SELECT_TIMEOUT = 0
BUFFER_SIZE = 1024

class Handler:
    # A handler is ready if its socket is ready to write.
    def __init__(self):
        dead = False
    def ready(self):
        return select([self.socket], [], [], SELECT_TIMEOUT)[0]

# with 'user'. Uses TCP only.
class UserHandler(Handler):
   def __init__(self, socket):
        # socket passed already be bound and connected (as returned by accept())
        self.socket = socket
    def sendAUR(self):
        raise NotImplementedError
    def sendDLR(self):
        raise NotImplementedError
    def sendBKR(self):
        raise NotImplementedError
    def sendRSR(self):
        raise NotImplementedError
    def sendLDR(self):
        raise NotImplementedError
    def sendLFD(self):
        raise NotImplementedError
    def sendDDR(self):
        raise NotImplementedError
    def parse(self):
        raise NotImplementedError
    def idle(self):
        raise NotImplementedError
    def check(self):
        if self.ready(self)
            handle()

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
        raise NotImplementedErroR

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

def main():
    if '-p' in argv:
        port = argv[index('-p') + 1]
    else:
        port = 58056 
    print('Using port', port)
    NewHandler = nh(port)
    nh.start()
 
if __name__ == '__main__':
    main()
