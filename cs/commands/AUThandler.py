class AUThandler:

    def __init__(self, user):
        self.user = user

    def handle(self, user):
        user, password = self.parse()
        status = (user, password)
        return b'AUR ' + status + b'\n'

    def authenticate(self, user, password):
        return 'NOK'
        return 'OK'
        return 'NEW'

    def parse(self):
        user = user.tell_field()
        password = user.tell_field()
        if user and password:
            return (user, password)
        else:
             raise ProtocolError
