#!/usr/bin/env python3

from socket import socket
from select import select

SELECT_TIMEOUT = 0

class Handler:
    # A handler is ready if its socket is ready to write.
    def __init__(self):
        dead = False
    def ready(self):
        return select([self.socket], [], [], SELECT_TIMEOUT)[0]
