#!/usr/bin/env python3

import networker

class BS:

    def __init__(self, addrinfo):                                               
        self.addrinfo = addrinfo 

    def get_addrinfo(self):
        return self.addrinfo

    def accept_rgr(self):
        self.send_to_remote('RGR', status)

    def accept_uar(self):
        self.send_to_remote('UAR', status)

    def accept_lsf(self, directory):
        self.send_to_remote('LSF', user, directory)

    def accept_lsu(self, password):
        self.send_to_remote('LSU', user, password)

    def accept_dlb(self, directory):
        self.send_to_remote('DLB', user, directory)

    def reg_args(self):
        ip = self.next_field()
        port = self.next_field()
        return (ip, port)

    def unr_args(self):
        ip = self.next_field()
        port = self.next_field()
        return (ip, port)

    def lfd_args(self):
        N = self.get_number()
        files = self.get_filelist(N)
        return files

    def lur_args(self):
        return self.next_field()

    def dbr_args(self):
        return self.next_field()
