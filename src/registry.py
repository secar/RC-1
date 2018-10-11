#!/usr/bin/env python3

from contextlib import contextmanager
import os

@contextmanager
def dir_as_working(new_dir):
    prev_dir = os.getcwd()
    os.chdir(os.path.expanduser(new_dir))
    try:
        yield
    finally:
        os.chdir(prev_dir)

### These directories must end in a slash, and must never be equal. ###
_BASEDIR = './registry/'
_PASSDIR = _BASEDIR + 'passwords/'
_USERDIR = _BASEDIR + 'users/'

if not os.path.exists(_BASEDIR):
    os.mkdir(_BASEDIR)
if not os.path.exists(_PASSDIR):
    os.mkdir(_PASSDIR)
if not os.path.exists(_USERDIR):
    os.mkdir(_USERDIR)

### PUBLIC ### 

def add_user(n, password):
    _write_pass_file(n, password)
    _make_user_dir(n) 

def del_user(user):
    _delete_user_dir(user)    
    _delete_pass_file(user)    

def auth_user(user, password_given):
    password = _read_pass_file(user)
    return password_given == password

def add_file(user, name, ip, port):
    _write_bs_file(user, name, ip, port)

def del_file(user, name):
    _delete_bs_file(user, name)
        
def get_bs_addrinfo(user, filename):
    line = _read_bs_file(user, filename)
    return tuple(line.split())

### PRIVATE ###

def _read_pass_file(user):
    with dir_as_working(_PASSDIR):
        with open(user, mode='r') as f:
            return f.read()

def _write_pass_file(user, password):
    with dir_as_working(_PASSDIR):
        with open(user, mode='x') as f:
            f.write(password)

def _delete_pass_file(user):
    with dir_as_working(_PASSDIR):
        os.remove(user)

def _make_user_dir(user):
    with dir_as_working(_USERDIR):
        os.mkdir(user)

def _delete_user_dir(user):
    with dir_as_working(_USERDIR):
        os.rmdir(user)

def _read_bs_file(user, filename):
    with dir_as_working(_USERDIR + user):
        with open(filename, mode='r') as bsfile:
            return bsfile.read()

def _write_bs_file(user, filename, ip, port):
    with dir_as_working(_USERDIR + user):
        with open(filename, mode='x') as bsfile:
            bsfile.write(ip + ' ' + port)

def _delete_bs_file(user, name):
    with dir_as_working(_USERDIR + user):
        os.remove(name)
