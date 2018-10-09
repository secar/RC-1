import filectrl

def handle(user):
    try:
        filectrl.del_user(user.name)
        user.hear('DLR OK\n')
    except:
        user.hear('DLR NOK\n')
        
