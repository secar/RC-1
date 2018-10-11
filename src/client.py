class Client:

    def __init__(self, networker):
        self.networker = networker
    
    def handle(cs):
        cmd = self.next_field()
        cmd_to_handler[cmd]()

    def get_number(self):
        return self.next_field()
    
    def get_filelist(user, N):
        files = []                                                             
        for _ in range(N):
            name = user.next_field()
            date = user.next_field()    
            time = user.next_field()    
            size = user.next_field()
            line = name + ' ' + date ' ' + time + ' ' + size
            file_list.append(line)
        return files

    def next_field(self)
        return self.networking.recv_field()

    def send_to_remote(self, *args): 
        line = ' '.join(args)
        self.networker.send_line(line)
