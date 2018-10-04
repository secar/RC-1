#!/usr/bin/env python3

import socket
from sys import argv

# with 'user'
class UserHandler:
    socket = socket.socket(type=socket.SOCK_STREAM)
    def sendAUR():
        pass
    def sendDLR():
        pass
    def sendBKR():
        pass
    def sendRSR():
        pass
    def sendLDR():
        pass
    def sendLFD():
        pass
    def sendDDR():
        pass

# with 'BS'
class BSHandler:

   def __init__(self, socket)
        self.socket = socket
    def sendRGR():
        pass
    def sendUAR():
        pass
    def sendLSF():
        pass
    def sendLSU():
        pass
    def sendDLB():
        pass

def main():
    if '-p' in argv:
        port = argv[index('-p') + 1]
    else:
        port = 58056 
    print('Using port', port)

if __name__ == '__main__':
    main()
