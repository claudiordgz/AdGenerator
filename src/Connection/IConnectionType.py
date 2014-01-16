__author__ = 'Claudio'

class IConnectionType(object):
    """
    Every connection has a username and
    a password.
    """
    def __init__(self):
        self.username = ""
        self.password = ""

    def getUser(self):
        return self.username

    def getPassword(self):
        return self.password

    def __str__(self):
        return "Username is {uname}".format(uname=self.username)