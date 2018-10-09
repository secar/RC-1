class BCKhandler:

 def __init__(self, self.userhandler, bshandler):
    self.userhandler = userhandler   

 def handle(self):                                                         
    '''sends BKR'''
        directory, user_filespecs = parse()               
        bs = doorman.get_BS_by_dir(directory)
        bs_filespecs = bs.get_file_list()
        new_filespecs = user_filespecs - bs_filespecs 
        line = b'' 
        while new_filespecs:
            fs = newfilespecs.pop()
            line += fs + b' '
        return line + b'\n' 

    def parse(self):
        directory = get_directory()                                              
        N = get_N()                                                              
        user_filespecs = get_filespecs() 
        return (directory, user_filespecs)
                                                                             
    def get_directory(self):
        dir = user.tell()
        if dir:
            return dir
        else:
            raise ProtocolError
                                 
    def  get_N(self):
         N = user.tell() 
         if N.isdigit():
            return N
        else:
            raise ProtocolError
                                                                             
    def get_filespecs(self, N):                                        
        user_filespecs = set()                                                 
        for _ in range(N):                                             
            name = user.tell()                                     
            date = user.tell()                                         
            time = user.tell()                                         
            size = user.tell()                                         
            if filename and date and time and size:
                user_filespecs.add(FileSpec(filename, date, time, size))
            else:
                raise ProtocolError
        return user_filespecs                                                  
