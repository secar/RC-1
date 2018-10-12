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
            return user.User(addrinfo)
    elif udp_socket in ready:
        addrinfo = udp_socket.recvfrom(0)[1]
        c = clients.get(addrinfo)
        if c:
            return c
        else:
            return bs.BS(addrinfo)
    else:
        raise Exception

def read_field(client):
    byte  = self.read_byte()
    field = b''
    while byte not in (b' ', b'\n', b''):
        field += byte
        byte = self.read_byte()
    return field.decode()

def fix_line(line):
    if type(line) != bytes:
        line = line.encode()
    if line[-1] != b'\n':
        line = line + b'\n'
    return line

def send_line(target, line):
    if type(target) == User:
        socket = tcp_socket
    if type(target) == BS:
        socket = udp_socket
    line = fix_line(line)
    while line:
        if socket.sendto(line[0], target):
            line = line[1:]

def read_byte(origin):
    if type(target) == User:
        socket = tcp_socket
    if type(target) == BS:
        socket = udp_socket
    byte = socket.recv(1)
    while not byte:                                                      
        byte = socket.recvfrom(1, origin.get_addrinfo())
    return byte                                                              
