from TCP.server_tcp import TCPServer
from UDP.server_udp import UDPServer
from UDP.client_udp import UDPClient


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

    def serve_file_udp(self, host, port):
        """Function used to instantiate a UDP Server"""
        udp_server = UDPServer(host, port)
        udp_server.send_file()

    def receive_file_udp(self, host, port):
        """Function used to instantiate a UDP Server"""
        udp_server = UDPClient(host, port)
        udp_server.receive_file()