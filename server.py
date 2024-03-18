import socket
from mini_par_sint import run

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()

        print('Servidor MiniPar esperando por conexões...')
        conn, addr = self.server_socket.accept()
        with conn:
            print('Conexão estabelecida com', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                # Decodifica a mensagem recebida
                message = data.decode()

                # Separa os elementos da mensagem
                aux = ''
                for letter in message:
                    aux = aux + letter
                    if(aux == "CALCULADORA"):
                        # remove de 0 até i
                        message = message[len(aux):]
                        # chamar a função do cabral
                        result = str(run(message))
                        break
                    elif(aux == "SEQ FIBO" or aux == 'PAR FIBO'):
                        #message = message[i:]
                        # chamar a função do cabral
                        break
                    elif(aux == "SEQ FAT" or aux == 'PAR FAT'):
                        #message = message[i:]
                        # chamar a função do cabral
                        break

                # Envia o resultado para o cliente
                conn.sendall(result.encode())

    def close(self):
        self.server_socket.close()

def main():
    #Inicializa o servidor
    server = Server('localhost', 55555)
    server.start()
    
                  
if __name__ == "__main__":
    main()
