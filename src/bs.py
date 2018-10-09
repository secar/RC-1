import networking

 class BS:
    def __init__(self):
        self.addrinfo  = None
        self.sock = ClientSocket(BS)
    
    def get_command(self):
        pass

    def parse(self, cmd):
        pass
    
    def receive_rgr(self):
        self._receive_line('RGR', status) 

    def receive_uar(self):
        self._receive_line('UAR', status)

    def receive_lsf(self, user, directory):
        self._receive_line('LSF', user, directory)

    def receive_lsu(self, user, password):
        self._receive_line('LSU', user, password)

    def receive_dlb(self, user, directory):
        self._receive_line('DLB', user, directory)

    ### PRIVATE ###

    def _next_field(self)
        return networking.recv_field(self.sock)
