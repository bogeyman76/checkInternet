#pings google continually every 3 seconds until successful
#defaults to google DNS server on port 53 with a three second timeout

import socket

class checkInternet:
    def __init__(self,h='8.8.8.8',p=53,t=3):
        self.host = h
        self.port = p
        self.timeout = t
        self.connected = False
        self._checkInternet()
    
    def _checkInternet(self):
        while self.connected == False:
            self.connected = self.pingNet()

    def pingNet(self):
        try:
            socket.setdefaulttimeout(self.timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((self.host, self.port))
            return True
        except socket.error as ex:
            return False
