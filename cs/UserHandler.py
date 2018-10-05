#!/usr/bin/env python3

from socket import socket
from select import select

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
