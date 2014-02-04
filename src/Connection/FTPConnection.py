__author__ = 'Claudio'

import IConnectionType
import ftplib

class FTPConnection(IConnectionType.IConnectionType):

    def __init__(self, host="", protocol="", port=21):
        self.host = host
        self.protocol = protocol
        self.port = port

    def connect(self):
        self.ftp = ftplib.FTP(self.host)
        self.ftp.login(self.username, self.password)

    def close(self):
        self.ftp.close()

    def __str__(self):
        return "Connection | " \
               "Type: FTP | " \
               "Username: {user} | " \
               "Host: {host} | " \
               "Protocol: {port}".format(user=self.username, host=self.host, port=self.port)

