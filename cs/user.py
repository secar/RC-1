import cs
 
class User:

    def __init__(self):
        self.username  = None
        self.password  = None
        self.networker = Networker(self)
    
    def tell_line(line, self):
         networker.sendline(line)

    def hear_word(self):
        return networker.recv_field()
