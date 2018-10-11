#!/usr/bin/env python3

from socket import *
from select import *
from signal import *
import bs
import user

PORT = 50000
udp_socket = None
tcp_socket = None

### PUBLIC: ###

def cleanup():
    if tcp_socket:
        tcp_socket.close()
    if udp_socket:
        udp_socket.close()

def setup_sockets():
    global udp_socket
    global tcp_socket
    try:
        cleanup()
        tcp_socket = socket(family=AF_INET, type=SOCK_STREAM)
        tcp_socket.bind(('', PORT))
        tcp_socket.listen(20)
        udp_socket = socket(family=AF_INET, type=SOCK_DGRAM)
        udp_socket.bind(('', PORT))
    except:
        cleanup()
        raise
setup_sockets()


def client_select(clients):
    clients = {c.get_addrinfo(): c for c in clients}
    ready = select([tcp_socket, udp_socket], [], [])[0]
    if tcp_socket in ready:
        addrinfo = tcp_socket.accept()[1]
        c = clients.get(addrinfo)
        if c:
            return c
        else:
            return user.User(UserNetworker(addrinfo))
    elif udp_socket in ready:
        addrinfo = udp_socket.recvfrom(0)[1]
        c = clients.get(addrinfo)
        if c:
            return c
        else:
            return bs.BS(BSNetworker(addrinfo))
    else:
        raise Exception
            

class ClientNetworker: # Abstract

    def __init__(self):
        raise NotImplementedError

    def read_field(self):
        byte  = self.read_byte()
        field = b''
        while byte not in (b' ', b'\n', b''):
            field += byte
            byte = self.read_byte()
        return field.decode()

    def fix_line(self, line):
        if type(line) != bytes:
            line = line.encode()
        if line[-1] != b'\n':
            line = line + b'\n'
        return line

    def get_addrinfo(self):
        return self.addrinfo

class UserNetworker(ClientNetworker):

    def __init__(self, addrinfo):
        self.addrinfo = addrinfo

    def send_line(self, line):
        line = fix_line(line)
        while line:
            if self.socket.send(line[0]):
                line = line[1:]

    def read_byte(self):
        byte = self.socket.recv(1)
        while not byte:                                                      
            byte = self.socket.recv(1)                                               
        return byte                                                              

class BSNetworker(ClientNetworker):

    def __init__(self, addrinfo):
        self.addrinfo = addrinfo
        
    def send_line(self, line):
        line = fix_line(line)
        while line:
            if self.socket.sendto(line[0], self.peer_addrinfo):
                line = line[1:]

    def read_byte(self, peer_addrinfo):
        byte = udp_buffer.pop_buffer_byte(peer_addrinfo)
        while not byte:
            byte, received_addrinfo = self.socket.recvfrom(1) 
            if peer_addrinfo != received_addrinfo:
                self.udp_buffer.push_byte(byte)
                byte = None # not ours
        return byte

        




