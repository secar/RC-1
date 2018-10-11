import networker

class BS:
    self_parser_table = {
        '': _handle_reg
        '': _handle_unr
        '': _handle_lfd
        '': _handle_lur
        '': _handle_dbr
    }

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
