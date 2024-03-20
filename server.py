import socket
from mini_par_sint import run
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.result = []

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
                        # remove CALCULADORA
                        message = message[len(aux):]
                        # chamar a função do cabral
                        result = str(run(message))
                        break
                    elif(aux == "SEQ FIBO" or aux == 'PAR FIBO'):
                        # chamar a função do cabral
                        fib_str = '''
                            a = 0
                            b = 1
                            n = 10
                            i = 2
                            while(i < n)
                                c = a + b
                                a = b
                                b = c
                                i = i + 1
                            print(c)
                        '''
                        if aux == "SEQ FIBO":
                            result = str(run(fib_str))
                        else:
                            thread1 = threading.Thread(target = self.par_fib())
                            thread1.start()
                        break

                        break
                    elif(aux == "SEQ FAT" or aux == 'PAR FAT'):
                        # chamar a função do cabral
                        factorial_str = '''
                            n = 5;
                            f = 1;
                            while n > 1:
                                f = f * n;
                                n = n - 1;
                            print(f);
                            '''
                        if aux == "SEQ FAT":
                            result = str(run(factorial_str))
                        else:
                            thread1 = threading.Thread(target = self.par_fat())
                            thread1.start()
                        break

                # Envia o resultado para o cliente
                conn.sendall(result.encode())
    def par_fat(self):
        fib_str = '''
            a = 0
            b = 1
            n = 10
            i = 2
            while(i < n)
                c = a + b
                a = b
                b = c
                i = i + 1
            print(c)
        '''
        result = str(run(fib_str))
        self.result = result
        
    def par_fib(self):
        fib_str = '''
        n = 5;
        f = 1;
        while n > 1:
            f = f * n;
            n = n - 1;
        print(f);
        '''
        result = str(run(fib_str))
        self.result = result
             
    def close(self):
        self.server_socket.close()

def main():
    #Inicializa o servidor
    server = Server('localhost', 55555)
    server.start()
    
                  
if __name__ == "__main__":
    main()
