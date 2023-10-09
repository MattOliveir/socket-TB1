""" 
    NOMES: Alexya Silva, Gustavo Deon, Matheus Oliveira, Vittoria Presa

    REFERENCIAS:
        https://www.youtube.com/watch?v=BlQbUV_W954 [Python Socket Programming Tutorial 7 - TCP/IP Client and Server]
        https://docs.python.org/3/howto/sockets.html
        https://steelkiwi.com/blog/working-tcp-sockets/

        https://stackoverflow.com/questions/27893804/udp-client-server-socket-in-python
        https://wiki.python.org/moin/UdpCommunication
        https://pythontic.com/modules/socket/udp-client-server-example

        https://medium.com/@mryklief21/file-transfer-using-udp-sockets-in-python-d90a6ecfac82
        https://stackoverflow.com/questions/13993514/sending-receiving-file-udp-in-python
"""


from application_manager import ApplicationManager
from TCP.client_tcp import ClienteTCP
from UDP.client_udp import ClienteUDP


def menu_display():
    """Menu de Display com as opções de inicialização de cliente e servidor, tanto UDP quanto TCP"""
    print("1. Iniciar Cliente TCP")
    print("2. Iniciar Cliente UDP")
    print("3. Iniciar Servidor TCP")
    print("4. Iniciar Servidor UDP")
    print("5. Receber Arquivo UDP")
    print("6. Enviar Arquivo UDP")
    print("9. Sair")


def input_usuario():
    """Função que trata os inputs do usuário de acordo com sua escolha"""
    controleAplicacao = ApplicationManager()

    while True:
        menu_display()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            host = input("Insira o endereço IP do servidor: ")
            port = int(input("Insira a porta do servidor: "))
            cliente = ClienteTCP(host, port)
            cliente.run()

        elif escolha == '2':
            host = input("Insira o endereço IP do servidor: ")
            port = int(input("Insira a porta do servidor: "))
            cliente = ClienteUDP(host, port)
            cliente.run()

        elif escolha == '3':
            host = input(
                "Insira o endereço IP do servidor (deixe em branco para localhost): ")
            port = int(input("Insira a porta do servidor: "))
            controleAplicacao.gerencia_tcp(host, port)

        elif escolha == '4':
            host = input(
                "Insira o endereço IP do servidor (deixe em branco para localhost): ")
            port = int(input("Insira a porta do servidor: "))
            controleAplicacao.gerencia_udp(host, port)

        elif escolha == '5':
            host = input(
                "Insira o endereço IP do servidor: ")
            port = int(input("Insira a porta do servidor: "))
            controleAplicacao.receive_file_udp(host, port)

        elif escolha == '6':
            host = input(
                "Insira o endereço IP do servidor (deixe em branco para localhost): ")
            port = int(input("Insira a porta do servidor: "))
            controleAplicacao.serve_file_udp(host, port)

        elif escolha == '9':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    input_usuario()
