#!/usr/bin/env python3

from socket import * 
from select import select

class Bouncer:


    replies = { 
        b'AUT ': AUThandler,
        b'DLU ': DLUhandler,
        b'BCK ': BCKhandler,
        b'RST ': RSThandler,
        b'LSD ': LSDhandler,
        b'LSF ': LSFhandler,
        b'DEL ': DELhandler,
        b'REG ': REGhandler,
        b'UNR ': UNRhandler,
    } 

    def __init__(self):
        self.client_list = []
        self.networker = Networker()

    def wait(self):
        queue = networker.get_waiting_clients(client_list) # XXX: May block!
        for client in queue:
            command = client.tell_field()
            
            if not replies[command](client):
                client.hear('ERR\n') 


