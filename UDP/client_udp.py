"""Module for socket connection"""
import socket


class UDPClient:
    """Class for a TCP Client"""
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        """Runs the TCP client listening for host:port requests"""
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest = (self.host, self.port)
        print('Para sair use CTRL+X\n')
        msg = input()
        while msg != '\x18':
            udp.sendto(msg.encode('utf-8'), dest)
            msg = input()
        udp.close()
