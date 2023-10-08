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

    def send_file(self):
        ready_signal = ''
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest = (self.host, self.port)

        udp.bind(dest)

        while(ready_signal != 'ready'):
            ready_signal, _ = udp.recvfrom(1024)
            ready_signal = ready_signal.decode('utf-8')
        file_path = input("Enter the path of the file to send: ")
        try:
            udp.sendto('ready'.encode('utf-8'), dest)
            with open(file_path, 'rb') as file:
                data = file.read(1024)
                while data:
                    udp.sendto(data, dest)
                    data = file.read(1024)
                udp.sendto('Done'.encode('utf-8'), dest)
            print(f"File sent successfully to {dest}")
        except FileNotFoundError:
            print("File not found.")