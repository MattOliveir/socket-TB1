from TCP.server_tcp import TCPServer
from UDP.server_udp import UDPServer


class ApplicationManager:
    """Handles launching the desired module"""
    def __init__(self):
        pass

    def handle_tcp(self, host, port):
        """Function used to instantiate a TCP Server"""
        tcp_server = TCPServer(host, port)
        tcp_server.run()

    def handle_udp(self, host, port):
        """Function used to instantiate a UDP Server"""
        udp_server = UDPServer(host, port)
        udp_server.run()
