import socket
import sys
import threading

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('localhost', 55555))
        

    def receive(self):
        return self.client.recv(1024).decode('utf-8')

    def write(self,keyword):
        #codigo para mandar a mensagem para o server
        mensagem = keyword
        
        entrada = input("CODIGO: ")

        mensagem = mensagem + " " + entrada
        #montar aqui a requisição e enviar pelo sendall
        self.client.sendall(mensagem.encode())

        mensagem = self.receive()
        print(mensagem)

    
def main():
    #inicializa o cliente
    client = Client()

    #EXEMPLOS
            #CALCULADORA 1 * 5
            #PAR FIBO var = 5\n while
            #SEQ FIBO var = 5\N while
    
    while True:
        entrada = input("Qual operação iremos realizar? ")

        if entrada == 'CALCULADORA':
            client.write(entrada)

        elif entrada == "FIBO" or  entrada == "FAT":

            modo = input("SEQ ou PAR? ")
            if(modo == 'SEQ'):
                client.write("SEQ " + entrada)
            elif(modo == 'PAR'):
                client.write("PAR " + entrada)
            
        elif entrada == 'SAIR':
            break
            

if __name__ == "__main__":
    main()
