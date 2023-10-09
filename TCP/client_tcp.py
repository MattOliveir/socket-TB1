"""Modulo de conecção para o Socket de TCP"""
import socket

"""Definição de Classe para um cliente TCP"""
class ClienteTCP:
    
    """Roda o conteudo de TCP escutando a seguinte configuração de requisição: host:port"""
    def run(self):
        """Cria conecção de Socket"""
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        destino = (self.host, self.port)
        """Realiza conecção com o header de destino"""
        tcp.connect(destino)
        print('Para sair use CTRL+X\n')
        mensagem = input()
        while mensagem != '\x18':
            """Utilizando utf-8 devido ao Ç"""
            tcp.send(mensagem.encode('utf-8'))
            mensagem = input()
        tcp.close()

    """Inicializador do Modulo"""
    def __init__(self, host, port):
        self.host = host
        self.port = port
