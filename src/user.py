import networking
import client

class User(client.Client):

    cmd_to_handler = {
        'AUT': _handle_aut
        'DEL': _handle_del
        'RSF': _handle_rsf
        'BCK': _handle_bck
        'LSF': _handle_lsf
    }

    def accept_aur(self, status):
        self.send_to_remote('AUR', status) 

    def accept_dlr(self, status):
        self.send_to_remote('DLR', status) 

    def accept_bkr(self, ip, port, filespec_list):
        self.send_to_remote('BKR', ip, port, filespec_list) 

    def accept_rsr(self, ip, port):
        self.send_to_remote('RSR', ip, port) 

    def accept_ldr(self, N, dir_list):
        self.send_to_remote('LDR', N, dir_list) 

    def accept_lfd(self, ip, port, filespec_list):
        self.send_to_remote('LFD', ip, port, filespec_list) 

    def accept_ddr(self, status):
        self.send_to_remote('DDR', status)

    def _handle_aut(self, cs):
        cs.accept_aut(self, *self._parse_aut(self))
    def _handle_dlu(self, cs):
        cs.accept_dlu(self, *self._parse_aut(self))
    def _handle_rst(self, cs):
        cs.accept_rst(self, *self._parse_rst(self))
    def _handle_del(self, cs):
        cs.accept_del(self, *self._parse_del(self))
    def _handle_lsd(self, cs):
        cs.accept_lsd(self, *self._parse_lsd(self))

    def _parse_aut(self):
        self = self.next_field()
        password = self.next_field()
        if self and password:
            return (self, password)
        else:
             raise ProtocolError

    def _parse_dlu(self):
        return ()

    def _parse_bck(self):
        directory = self.next_field()
        N = self.get_number() 
        file_list = self.get_filelist(N)
        return (directory, N, file_list)
        
    def _parse_rst(self):
        directory = self.next_field()
        return (directory,)

    def _parse_del(self):
        directory = self.next_field()
        return (directory,)

    def _parse_lsf(self):
        directory = self.next_field()
        return (directory,)

    def _parse_lsd(self):
        return ()
