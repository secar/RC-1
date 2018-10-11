#!/usr/bin/python3

import networker

class BS:

    def __init__(self):
        self.cmd_to_handler = {
            'REG': self._handle_reg,
            'UNR': self._handle_unr,
            'LFD': self._handle_lfd,
            'LUR': self._handle_lur,
            'DBR': self._handle_dbr
        }

    def get_addrinfo(self):
        self.networker.getaddrinfo()

    def accept_rgr(self):
        self.networker.send_line('RGR', status) 

    def accept_uar(self):
        self.networker.send_line('UAR', status)

    def accept_lsf(self, user, directory):
        self.networker.send_line('LSF', user, directory)

    def accept_lsu(self, user, password):
        self.networker.send_line('LSU', user, password)

    def accept_dlb(self, user, directory):
        self.networker.send_line('DLB', user, directory)

    def _handle_reg(self):
        cs.accept_reg(self, *self._parse_reg(self))                              
    def _handle_unr(self):
        cs.accept_unr(self, *self._parse_unr(self))                              
    def _handle_lfd(self):
        cs.accept_lfd(self, *self._parse_lfd(self))                              
    def _handle_lur(self):
        cs.accept_lur(self, *self._parse_lur(self))                              
    def _handle_dbr(self):
        cs.accept_dbr(self, *self._parse_dbr(self))                              

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
        return (N, files)

    def _parse_lur(self):
        return self.get_number()

    def _parse_dbr(self):
        return self.get_number()
