__author__ = 'Claudio'


class IConnection(object):

    def __init__(self, type_strategy=None):
        if type_strategy:
            #get a handle to the object
            self.action = type_strategy()

    def load(self, username, password):
        pass