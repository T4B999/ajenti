import ajenti
from ajenti.api import *
from passlib.hash import sha512_crypt


@plugin
class UserManager (object):
    def check_password(self, username, password):
        if not username in ajenti.config.tree.users:
            return False
        type = 'plain'
        saved = ajenti.config.tree.users[username].password
        if '|' in saved:
            type, saved = saved.split('|')

        if type == 'plain':
            hash = password
        else:
            hash = self.hash_password(password)

        return hash == saved

    def hash_password(self, password):
        if not password.startswith('sha512|'):
            password = 'sha512|%s' % sha512_crypt.encrypt(password)
        return password
