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

    def receive_file(self):
        ready_signal = ""
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest = (self.host, self.port)

        file_path = input("Enter the path to save the received file: ")

        udp.sendto('ready'.encode('utf-8'), dest)

        while(ready_signal != 'ready'):
            ready_signal, _ = udp.recvfrom(1024)
            ready_signal = ready_signal.decode('utf-8')
        try:
            with open(file_path, 'wb') as file:
                while True:
                    data, _ = udp.recvfrom(1024)
                    print(data)
                    if data == b'File not found':
                        print("File not found on the server.")
                        break
                    elif data.decode('utf-8') == 'Done':
                        print(f"File received successfully from {dest}")
                        break
                    file.write(data)
        except Exception as e:
            print(f"An error occurred: {e}")