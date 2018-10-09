#!/usr/bin/env python3

from socket import * 
from select import select
import networking

replies = { 
    'DLU': handle_dlu,
    'BCK': handle_bck,
    'RST': handle_rst,
    'LSD': handle_lsd,
    'LSF': handle_lsf,
    'DEL': handle_del,
    'UNR': handle_unr,
} 

global _active_bs_list = []
global _active_user_list = []

def register(bs):
    _bs_list.append(bs)

def unregister(bs):
    _bs_list.delete(bs)

def login(user):
    _user_list.append(bs)

def logout(user):
    _user_list.delete(bs)

def service_loop(self):
    ready = networking.client_select(client_list) # XXX: May block!
    check_new(ready)
    service_clients(ready)

def service_clients():
    if bs_socket in ready:
        new_bs = greet_bs(bs_socket)
    if user_socket in ready: 
        new_user = greet_user(user_socket)
    for client in queue:
        command = client.tell_field()
        try: 
            self.replies[command](client)
        except KeyError:
            client.hear('ERR\n')

def greet_bs(entry_socket):
'''the socket should be UDP and ready to use'''
    new_bs = bs.BS(entry_socket)
    if handle_reg(new_bs):
        return new_bs

def greet_user(entry_socket):
'''the socket should be TCP and ready to use'''
    new_s = entry_socket.accept()[0]
    new_user = user.User(new_s)
    if handle_aut(new_user):
        return new_user

# User: XXX code missing

def do_aut(user, name, password):
    if register.auth_user(name, password):
        user.setname(name)                                                       
        user.setpassword(password)                                               
        status = 'OK'
    else:
        status = 'NOK'
    user.receive_aur(status)

def do_dlu(user):
    if register.delete_user(user):
        status = 'OK'
        user.die()
    else:
        status = 'NOK'
    user.receive_dlr(status)

def do_bck(user, directory, N, files_list):
    bs = registry.get_bs(directory)
    bs.receive_lsf()   # in this
    user.receive_bkr() # order.

def do_lsf(user, directory):
    bs.receive_lsf()
    user.receive_dlr()
    user.receive_lfd()

def do_del(user, directory):
    bs = registry.get_bs(directory)
    bs.receive_dlb()
    user.receive_ddr()

# BS: XXX code missing

def do_reg(bs, ip, port):
    bs.receive_rgr()

def do_unr(bs, ip, port):
    bs.receive_uar()
