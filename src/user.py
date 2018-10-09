import networking

class User:

    self_parser_table = {
        'AUT': _self_parse_aut
        'DEL': _self_parse_del
        'RSF': _self_parse_rsf
        'BCK': _self_parse_bck
        'LSF': _self_parse_lsf
    }

    def __init__(self, simple_socket):
        self.username  = None
        self.password  = None
        self.socket = 
    
    def get_command(self):
        return self._get_next_field()

    def self_parse(self, command):
        self.self_parser_table[command](self)

    def receive_aur(self, status):
        self._receive_line('AUR', status) 

    def receive_dlr(self, status):
        self._receive_line('DLR', status) 

    def receive_bkr(self, ip, port, filespec_list):
        self._receive_line('BKR', ip, port, filespec_list) 

    def receive_rsr(self, ip, port):
        self._receive_line('RSR', ip, port) 

    def receive_ldr(self, N, dir_list):
        self._receive_line('LDR', N, dir_list) 

    def receive_lfd(self, ip, port, filespec_list):
        self._receive_line('LFD', ip, port, filespec_list) 

    def receive_ddr(self, status):
        self._receive_line('DDR', status)


    ### PRIVATE ###


    def _next_field(self)
        return networking.recv_field()

    def _self_parse_aut(user):
        user = user.next_field()
        password = user.next_field()
        if user and password:
            return (user, password)
        else:
             raise ProtocolError

    def _self_parse_dlu(user):
        return ()

    def _self_parse_bck(user):
            directory = user.next_field()
            N = user.next_field() 
            #if N.isdigit():
            file_list = []                                                             
            for _ in range(N):
                name = user.next_field()
                date = user.next_field()    
                time = user.next_field()    
                size = user.next_field()
                line = name + ' ' + date ' ' + time + ' ' + size
                file_list.append(line)
            return (directory, N, file_list)
        
    def _self_parse_rst(self):
        directory = user.next_field()
        return (directory,)

    def _self_parse_del(user):
        directory = user.next_field()
        return (directory,)

    def _self_parse_lsf(self):
        directory = user.next_field()
        return (directory,)

    def _self_parse_lsd(user):
        return ()
