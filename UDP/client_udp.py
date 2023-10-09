"""Modulo de conecção para o Socket de UDP"""
import socket

"""Definição de Classe para um cliente UDP"""
class ClienteUDP:

    """Roda o conteudo de UDP escutando a seguinte configuração de requisição: host:port"""
    def run(self):
        """Cria conecção de Socket"""
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        destino = (self.host, self.port)
        print('Para sair use CTRL+X\n')
        mensagem = input()
        while mensagem != '\x18':
            """Utilizando utf-8 devido ao Ç"""
            udp.sendto(mensagem.encode('utf-8'), destino)
            mensagem = input()
        udp.close()

    """Inicializador do Modulo"""
    def __init__(self, host, port):
        self.host = host
        self.port = port


    """ -- TENTATIVA DE RECEBER ARQUIVOS ---"""

    """Receptor de Files/Arquvos de texto"""
    def receive_file(self):
        ready_signal = ""
        """Cria conecção de Socket"""
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        destino = (self.host, self.port)

        """Caminho da salvamento do arquivo alvo"""
        file_path = input("Enter the path to save the received file: ")

        udp.sendto('ready'.encode('utf-8'), destino)

        while(ready_signal != 'ready'):
            ready_signal, _ = udp.recvfrom(1024)
            ready_signal = ready_signal.decode('utf-8')
        try:
            with open(file_path, 'wb') as file:
                while True:
                    data, _ = udp.recvfrom(1024)
                    print(data)
                    if data == b'File not found':
                        print("Arquivo não encontrado no Servidor.")
                        break
                    elif data.decode('utf-8') == 'Done':
                        print(f"Arquivo recebido com sucesso de {destino}")
                        break
                    file.write(data)
        except Exception as e:
            print(f"An error occurred: {e}")