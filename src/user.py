#!/usr/bin/env python3

import networking
import client

class User(client.Client):

    def __init__(self, addrinfo):                                               
        self.addrinfo = addrinfo

    def accept_aur(self, status):
        self.send_to_remote('AUR', status) 

    def accept_dlr(self, status):
        self.send_to_remote('DLR', status) 

    def accept_bkr(self, ip, port, filelist):
        self.send_to_remote('BKR', ip, port, filelist)

    def accept_rsr(self, ip, port):
        self.send_to_remote('RSR', ip, port) 

    def accept_ldr(self, N, dir_list):
        self.send_to_remote('LDR', N, dir_list) 

    def accept_lfd(self, ip, port, filelist):
        self.send_to_remote('LFD', ip, port, ' '.split(filelist)) 

    def accept_ddr(self, status):
        self.send_to_remote('DDR', status)

    def aut_args(self):
        self = self.next_field()
        password = self.next_field()
        if self and password:
            return (self, password)
        else:
             raise ProtocolError

    def dlu_args(self):
        return None

    def bck_args(self):
        directory = self.next_field()
        N = self.number() 
        file_list = self.filelist(N)
        return file_list
        
    def rst_args(self):
        directory = self.next_field()
        return directory

    def del_args(self):
        directory = self.next_field()
        return directory

    def lsf_args(self):
        directory = self.next_field()
        return directory
