#!/usr/bin/env python3

import networker

class BS:

    def __init__(self, networker):                                               
        self.networker = networker    

    def get_addrinfo(self):
        self.networker.getaddrinfo()

    def accept_rgr(self):
        self.networker.send_to_remote('RGR', status)

    def accept_uar(self):
        self.networker.send_to_remote('UAR', status)

    def accept_lsf(self, directory):
        self.networker.send_to_remote('LSF', user, directory)
        cs.accept_lfd(self, args)

    def accept_lsu(self, password):
        self.networker.send_to_remote('LSU', user, password)
        cs.accept_lur(self, args)

    def accept_dlb(self, directory):
        self.networker.send_to_remote('DLB', user, directory)

    def _parse_reg(self):
        ip = self.next_field()
        port = self.next_field()
        return (ip, port)

    def _parse_unr(self):
        ip = self.next_field()
        port = self.next_field()
        return (ip, port)

    def _parse_lfd(self):
        N = self.get_number()
        files = self.get_filelist(N)
        return files

    def _parse_lur(self):
        return (self.next_field(),)

    def _parse_dbr(self):
        return (self.next_field(),)
