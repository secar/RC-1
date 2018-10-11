#!/usr/bin/env python3

from socket import socket
from select import select
import bs
import user

PORT = None

### PUBLIC: ###

def tcp_socket(port):                                                          
    s = socket(AF_INET, SOCK_STREAM)                           
    s.bind((gethostname(), port))
    s.listen(20)
    return s

def udp_socket(port):                                                          
    s = socket(AF_INET, SOCK_DGRAM)                            
    s.bind((gethostname(), port)) 
    return s

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

    def fix_line(self, line)
        if type(line) != bytes:
            line = line.encode()
        if line[-1] != b'\n':
            line = line + b'\n'
        return line

    def die(self):                                                               
        self.socket.close()                                                      
        self.socket = None                                                       

class UserNetworker(ClientNetworker):
    socket = tcp_socket()

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

    socket = udp_socket()
    udp_buffer = {}

    def pop_buffer_byte(self, addrinfo):
        return self.udp_buffer.pop(addrinfo)

    def push_buffer_byte(self, addrinfo, byte):
            if self.udp_buffer.get(addrinfo):
                self.b[addrinfo] += byte
            else:
                self.b[addrinfo] = byte
        
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
    user_greeter = tcp_socket(PORT)
    bs_greeter = udp_socket(PORT)

    def die(self):                                                               
        self.user_greeter.close()
        self.bs_greeter.close()
        self.user_greeter = None 
        self.bs_greeter = None

    def read_select(sockets):
        return select(sockets, [], [])[0]
    
    def greet_user():
        new_s = self.user_greeter.accept()[0]
        u = user.User(UserNetworker(new_s))
        self.user_greeter.close()
        self.user_greeter = tcp_socket(PORT)
        return u

    def greet_bs():
        new_s = self.bs_greeter.dup()
        bs = bs.BS(BSNetworker(new_s))
        self.bs_greeter.close()
        self.bs_greeter = udp_socket(PORT)
        return bs

    def client_select(clients):
        soc_to_cli= {c.networker.socket: c for c in clients}
        ready_s = read_select(
            list(cli_soc.keys()) + [self.user_greeter + self.bs_greeter]) 
        ready_c = [soc_to_cli[s] for s in ready_s]
        if self.user_greeter in ready_s:
             ready_c.append(greet_user())
        if self.bs_greeter in ready_s:
            ready_c.append(greet_bs())
        return ready_c
