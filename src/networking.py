#!/usr/bin/env python3

from socket import socket
from select import select

'''content format is addrinfo:bufferstring'''

class udp_buffer:
    def __init__(self):
        self.b = {}

    def get_byte(self, addrinfo):
        return self.b.get(addrinfo)

    def push_byte(self, addrinfo, byte):
        try:
            self.b[addrinfo] += byte
        except KeyError:
            self.b[addrinfo] = byte

udp_buffer = udp_buffer()
PORT = None

bs_greeter = getUDPsocket(PORT)
user_greeter = getTCPsocket(PORT)

def get_waiting_clients(clients):
    readable = select(sockets + bs_greeter + user_greeter, [], [])[0]
    if bs_greeter in readable:
         [BS()] + readable
    if user_greeter in readable:
        [User()] + readable
   return readable 

class ClientSocket:

### PUBLIC: ###

    def __init__(self, client):
        if type(client) == User:
            self.socket = _setupTCP(PORT)
        elif type(client) == BS:
            self.socket = _setupUDP(PORT)
        else
            raise ValueError

    def client_select(readers)
        # receVives clients

    def recv_field(self):
        byte  = self._recv_byte()
        field = b''
        while byte not in (b' ', b'\n', b''):
            field += byte
            byte = self._recv_byte()
        return field 

    def send_line(self, line)
        if line[-1] != b'\n':
            raise ValueError('Passed line must end in a newline.')
        elif self.peer_addrinfo and self.socket.type == SOCK_STREAM:
            return self._stcp()
        else:
            return self._sudp()

    def die(self):                                                               
        self.socket.close()                                                      
        self.socket = None                                                       

### PRIVATE: ###

    def _stcp(self, line):
        while line:
            if self.socket.send(line[0]):
                line = line[1:]

    def _sudp(self, line):
        while line:
            if self.socket.sendto(line[0], self.peer_addrinfo):
                line = line[1:]

    def _recv_byte(self):
        if self.peer_addrinfo and self.socket.type == SOCK_STREAM:
            return _rtcp()
        else:
            return _rudp()

    def _rtcp(self):
        byte = self.socket.recv(1)
        while not byte:                                                      
            byte = self.socket.recv(1)                                               
        return byte                                                              

    def _rudp(self, peer_addrinfo):
        byte = udp_buffer.get_byte(peer_addrinfo)
        while not byte:
            byte, received_addrinfo = self.socket.recvfrom(1) 
            if peer_addrinfo != received_addrinfo:
                udp_buffer.push_byte(byte)
                byte = None # not ours
        return byte

def getTCPsocket(port):                                                          
    s1 = socket(AF_INET, SOCK_STREAM)                           
    s1.setblocking(0)                                           
    s1.bind((gethostname(), port))
    s1.listen(20) 
    return s1

def getUDPsocket(port):                                                          
    s = socket(AF_INET, SOCK_DGRAM)                            
    s.setblocking(0)                                           
    s.bind((gethostname(), port)) 
    return s
