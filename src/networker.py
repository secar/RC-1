#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, gethostname
from select import select
import bs
import user

PORT = 50000

### PUBLIC: ###

udp_buffer = {}
_udp_socket = None

def tcp_socket():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((gethostname(), PORT))
    s.listen(20)
    return s

def udp_socket():
    global _udp_socket
    if not _udp_socket:
        _udp_socket = socket(AF_INET, SOCK_DGRAM)                            
        _udp_socket.bind((gethostname(), PORT)) 
    return _udp_socket

def pop_buffer_byte(self, addrinfo):
    return udp_buffer.pop(addrinfo)

def push_buffer_byte(self, addrinfo, byte):
        if udp_buffer.get(addrinfo):
            udp_buffer[addrinfo] += byte
        else:
            udp_buffer[addrinfo] = byte

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

    def die(self):                                                               
        self.socket.close()                                                      
        self.socket = None

    def get_addrinfo(self):
        return self.socket.getsockname()

class UserNetworker(ClientNetworker):

    def __init__(self):
        self.socket = tcp_socket()

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

    def __init__(self):
        self.socket = udp_socket()
        
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

class CSNetworker:

    def __init__(self):
        self.user_greeter = tcp_socket()
        self.bs_greeter = udp_socket()

    def die(self):                                                               
        self.user_greeter.close()
        self.bs_greeter.close()
        self.user_greeter = None 
        self.bs_greeter = None

    def read_select(self, sockets):
        return select(sockets, [], [])[0]
    
    def greet_user(self):
        new_s = self.user_greeter.accept()[0]
        self.user_greeter.close()
        u = user.User(UserNetworker(new_s))
        self.user_greeter = tcp_socket()
        return u

    def greet_bs(self):
        new_s = self.bs_greeter.dup()
        bs = bs.BS(BSNetworker(new_s))
        self.bs_greeter = udp_socket()
        return bs

    def client_select(self, clients):
        soc_to_cli= {c.networker.socket: c for c in clients}
        ready_s = self.read_select(
            list(soc_to_cli.keys()) + [self.user_greeter, self.bs_greeter]) 
        ready_c = [soc_to_cli[s] for s in ready_s]
        if self.user_greeter in ready_s:
             ready_c.append(greet_user())
        if self.bs_greeter in ready_s:
            ready_c.append(greet_bs())
        return ready_c
