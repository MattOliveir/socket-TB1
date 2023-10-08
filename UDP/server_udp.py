"""Module for socket connection"""
import socket


class UDPServer:
    """Class for a TCP Server"""
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        """Runs the TCP client sending requests for host:port"""
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        orig = (self.host, self.port)
        udp.bind(orig)
        while True:
            msg, cliente = udp.recvfrom(1024)
            print(cliente, msg)
        udp.close()
