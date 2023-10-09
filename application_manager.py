from TCP.server_tcp import ServidorTCP
from UDP.server_udp import ServidorUDP
from UDP.client_udp import ClienteUDP


class ApplicationManager:
    """Gerencidor de instancias"""

    def gerencia_udp(self, host, port):
        """Cria uma Instancia do Servidor de UDP"""
        servidor_udp = ServidorUDP(host, port)
        servidor_udp.run()

    def gerencia_tcp(self, host, port):
        """Cria uma Instancia do Servidor de TCP"""
        servidor_tcp = ServidorTCP(host, port)
        servidor_tcp.run()

    """Modulos de envio de Arquivo"""

    def serve_file_udp(self, host, port):
        """Cria uma Instancia do Servidor de UDP"""
        servidor_udp = ServidorUDP(host, port)
        servidor_udp.send_file()

    def receive_file_udp(self, host, port):
        """Cria uma Instancia do Cliente de UDP para envio de Arquivos"""
        servidor_udp = ClienteUDP(host, port)
        servidor_udp.receive_file()

    """Inicializa o modulo escolhido"""
    def __init__(self):
        pass
