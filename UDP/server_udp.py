"""Modulo de conecção para o Socket de UDP"""
import socket

"""Definição de Classe para um Servidor UDP"""
class ServidorUDP:

    """Roda o conteudo de UDP escutando a seguinte configuração de requisição: host:port"""
    def run(self):
        """Cria conecção de Socket"""
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        origem = (self.host, self.port)
        udp.bind(origem)
        while True:
            mensagem, cliente = udp.recvfrom(1024)
            print(cliente, mensagem)
        udp.close()

    """Inicializador do Modulo"""
    def __init__(self, host, port):
        self.host = host
        self.port = port


    """ --- APARENTEMENTE FUNCIONA ? --- """

    """Sender de Files/Arquvos de texto"""
    def send_file(self):
        ready_signal = ''
        """Cria conecção de Socket"""
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        destino = (self.host, self.port)

        udp.bind(destino)

        while(ready_signal != 'ready'):
            ready_signal, _ = udp.recvfrom(1024)
            """Utilizando utf-8 devido ao Ç"""
            ready_signal = ready_signal.decode('utf-8')
        file_path = input("Enter the path of the file to send: ")
        try:
            udp.sendto('ready'.encode('utf-8'), destino)
            with open(file_path, 'rb') as file:
                data = file.read(1024)
                while data:
                    udp.sendto(data, destino)
                    data = file.read(1024)
                udp.sendto('Done'.encode('utf-8'), destino)
            print(f"Arquivo enviado com sucesso para {destino}")
        except FileNotFoundError:
            print("Arquivo não encontrado.")