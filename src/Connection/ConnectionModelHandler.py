__author__ = 'Claudio'

import yaml

class ConnectionHandler(object):
    """ The Connection Handler must handle all the I/O
        operations to the User Communications model.
    """
    def __init__(self):
        self.modify_lst = list()
        self.flags = dict()
        self.__modify_model = { 'ftp' : self.__model_ftp,
                       'dropbox': self.__model_dropbox,
                       'sugarsync': self.__model_sugarsync,
                       'onedrive': self.__model_onedrive
        }

    def get_model(self, yaml_file):
        stream = open(yaml_file, 'r')
        self.model = yaml.load(stream)
        stream.close()
        self.setup()

    def save_model(self, yaml_file):
        for key, val in self.flags.iteritems():
            self.model[key] = val
        if self.modify is True:
            for protocol in self.modify_lst:
                self.__modify_model[protocol]()
                print self.model
        with open(yaml_file, 'w') as yaml_fd:
            yaml_fd.write( yaml.dump(self.model, default_flow_style=False))

    def setup(self):
        if self.model:
            self.get_ftp()
            self.get_dropbox()
            self.get_onedrive()
            self.get_sugarsync()
        self.model.clear()

    def get_ftp(self):
        self.ftp = self.get_config('has_ftp', 'ftp')

    def modify_ftp(self, username, host, password, port):
        self.ftp['username'] = username
        self.ftp['host'] = host
        self.ftp['password'] = password
        self.ftp['port'] = port
        if self.flags['has_ftp'] is not True:
            self.flags['has_ftp'] = True
        self.modify = True
        self.modify_lst.append('ftp')

    def get_dropbox(self):
        self.dropbox = self.get_config('has_dropbox', 'dropbox')

    def get_sugarsync(self):
        self.sugarsync = self.get_config('has_sugarsync', 'sugarsync')

    def get_onedrive(self):
        self.onedrive = self.get_config('has_onedrive', 'onedrive')

    def get_config(self, has_config_str, config_str):
        if has_config_str not in self.flags:
            self.flags[has_config_str] = ''
        if has_config_str in self.model:
            if self.model[has_config_str] is True:
                self.flags[has_config_str] = True
                return_val = self.model[config_str]
            else:
                self.flags[has_config_str] = False
                return_val = dict()
        return return_val

    def __model_ftp(self):
        if 'ftp' not in self.model:
            self.model['ftp'] = dict()
        self.model['ftp']['username'] = self.ftp['username']
        self.model['ftp']['host'] = self.ftp['host']
        self.model['ftp']['password'] = self.ftp['password']
        self.model['ftp']['port'] = self.ftp['port']

    def __model_dropbox(self):
        pass

    def __model_sugarsync(self):
        pass

    def __model_onedrive(self):
        pass