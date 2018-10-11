#!/usr/bin/env python3

import networker

class CS:
    networker = networker.CSNetworker()
    active_bs_list = []
    active_user_list = []

    def accept_aut(user, name, password):
        if register.auth_user(name, password):
            user.setname(name)                                                       
            user.setpassword(password)                                               
            self.active_BS_list.append()
            status = 'OK'
        else:
            status = 'NOK'
            status = 'NEW'
        user.receive_aur(status)

    def accept_dlu(user):
        if register.delete_user(user.name):
            status = 'OK'
            user.die()
            self.active_BS_list.remove(bs)
        else:
            status = 'NOK'
        user.receive_dlr(status)

    def accept_bck(user, directory, N, files_list):
        bs = registry.get_bs(directory)
        bs.accept_lsf(directory)   # in this
        bs.execute(cs)

    def accept_lsf(user, directory):
        bs = registry.get_bs(directory)
        bs.receive_lsf(directory)
        bs.execute(cs)

    def accept_del(user, directory):
        bs_addrinfo = registry.get_bs(directory)
        bs.receive_dlb()
        user.receive_ddr()
        bs.execute(cs)

    def accept_reg(bs):
        ip, port = bs.get_line()
        bs.set_port(ip)
        bs.set_ip(port)
        _active_BS_list.append(bs)
        bs.receive_rgr(status)

    def accept_unr(bs):
        ip, port = bs.get_line()
        _active_BS_list.append(bs)
        status = 'OK'
        bs.receive_uar(status

    def start(self):
        ready = self.networker.client_select(client_list) # XXX: May block!
        for c in ready:
            c.execute(self)

def main():
    cs = CS()
    cs.start()

if __name__ == '__main__':
    main()
