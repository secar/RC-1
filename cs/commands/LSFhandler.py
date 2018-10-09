import filecntrl

def handleLFD(self):
    N = get_N()
    user_filespecs = get_filespecs(N)
    return (directory, user_filespecs)
                                                                         
def LFD_get_N():
     N = user.tell()
     if N.isdigit():
        return N
    else:
        raise ProtocolError
                                                                         
def LFD_get_filespecs():
    bs_filespecs = ''
    for _ in range(N):
        name = user.tell()
        date = user.tell()
        time = user.tell()
        size = user.tell()
        if name and date and time and size:
            user_filespecs.add(FileSpec(filename, date, time, size))
        else:
            raise ProtocolError
    return bs_filespecs

def sendLSF(bs, dir):
    bs.tell('LSF ' + dir)

def parse(user):
    return user.tell()

def handle(user):
    dir = parse(user)
    bs = filectrl.get_bs(dir)
    sendLSF(bs, dir)
    filelist = handleLFD(bs)
    send
    

