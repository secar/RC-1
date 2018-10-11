#!/usr/bin/env python3

import networker
import registry

class CS:
    networker = networker.CSNetworker()
    active_bs_list = []
    active_user_list = []

    def __init__(self, networker):
        self.networker = networker

    def accept_aut(user, name, password):
        status = registry.auth_user(name, password)
        if status != 'NOK':
            user.name = name
            user.password = password
            self.active_user_list.append(user)
        user.receive_aur(status)

    def accept_lur(user):
        user.accept_
        
    def accept_dlu(user):
        if registry.delete_user(user.name):
            status = 'OK'
            self.active_user_list.remove(user)
        else:
            status = 'NOK'
        user.receive_dlr(status)
        user.die()

    def accept_bck(user, directory, N, files_list):
        bs = self.get_bs(registry.get_bs(directory))
        bs.accept_lsf(directory)   # in this
        filelist = lsf_args()[0]
        self.accept_lfd(bs, user)
        ip, port = bs.get_addrinfo()

    def accept_lfd(user, bs, files):
        files = bs.lfd_args()
        user.accept_lfd(files)

    def accept_lsf(user, directory):
        bs = self.get_bs(user, directory)
        bs.receive_lsf(user.name, directory)
        assert(bs.get_cmd() == 'LFD')
        accept_lfd(user, files)

    def get_bs(user, directory):
        addrinfo = get_bs_addrinfo()
        for bs in self.active_bs_list:
            if addrinfo == bs.get_addrinfo():
                return bs        

    def accept_dbr(user, bs, status):
        status = bs.dbr_args()
        user.accept_dlr(status)

    def accept_del(user, directory):
        bs = self.get_bs(user, directory)
        bs.receive_dlb(user.name, directory)
        assert(bs.get_cmd() == 'DBR')
        bs.accept_dbr(bs)

    def accept_lsd(self, user):
        files = registry.user_files(user)
        user.accept_ldr(files)

    def accept_reg(self, bs, ip, port):
        bs.set_port(ip)
        bs.set_ip(port)
        self.active_bs_list.append(bs)
        status = 'OK'
        bs.receive_rgr(status)

    def accept_unr(bs, ip, port):
        addrinfo = bs.uar_args()
        bs = get_bs(addrinfo)
        self.active_bs_list.append(bs)
        status = 'OK'
        bs.receive_uar(status)

    def start(self):
        call_table = {                                                  
            'REG': self.accept_reg,                             
            'UNR': self.accept_unr,                                              
            'LFD': self.accept_lfd,                                              
            'DBR': self.accept_dbr,
            'UNR': self.accept_unr,
            'LSD': self.accept_lsd,
            'BCK': self.accept_bck
        }                                                                        
        ready = self.networker.client_select(
            self.active_user_list + self.active_bs_list) # XXX: May block!
        for c in ready:
            cmd = c.get_cmd()
            args = parse(cmd)
            call_table[cmd](c, *args)

def main():
    cs = CS()
    cs.start()

if __name__ == '__main__':
    main()
