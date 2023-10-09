"""Modulo de conecção para o Socket de TCP"""
import socket

"""Definição de Classe para um servidor TCP"""
class ServidorTCP:

    """Roda o conteudo de TCP escutando a seguinte configuração de requisição: host:port"""
    def run(self):
        """Cria conecção de Socket"""
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        origem = (self.host, self.port)
        tcp.bind(origem)

        """listen() - It defines the length of the backlog queue, which is the number of incoming connections
        that have been completed by the TCP/IP stack but not yet accepted by the application."""
        tcp.listen(1)
        while True:

            """accept() method blocks execution and waits for an incoming connection. When a client connects, 
            it returns a new socket object representing the connection and a tuple holding the address of the client. 
            The tuple will contain (host, port) for IPv4 connections """
            conexao, cliente = tcp.accept()
            print('Conectado por', cliente)
            while True:
                """ Receiver and buffer de 1024 bytes de leitura"""
                msg = conexao.recv(1024)
                if not msg:
                    break
                print(cliente, msg)
            print('Finalizando conexao do cliente', cliente)
            conexao.close()

    """Inicializador do Modulo"""
    def __init__(self, host, port):
        self.host = host
        self.port = port