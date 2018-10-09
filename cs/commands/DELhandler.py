import filectrl

### PRIVATE ###

def sendDLB(bs, dir, name):
    bs.hear('DLB ' + dir + name)

def sendDDR(user, success):
    reply = 'DDR OK' if success else 'DDR NOK'
    user.hear(reply)
    
def handleDBR(user, bs):
    sendDDR(bs.tell() == 'DBR' and bs.tell() == 'OK')

def parse(user):
    return user.tell()

### PUBLIC ###

def handle(user):
    dir = parse()
    bs = networking.get_bs(user, dir)
    sendDLB(bs, dir, user.name)
    handleDBR(user, bs)
