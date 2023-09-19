import socket  # Importa il modulo socket per la comunicazione di rete
import codecs  # Importa il modulo codecs per la codifica e decodifica dei caratteri

HOST = '192.168.90.101'
PORT = 7777


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket TCP/IP


client_socket.connect((HOST, PORT))  # Connettiti al server

encoding = 'cp1252'  # Codifica dei caratteri Windows-1252

while True:
    
    command = input('Inserisci un comando: ')  # Richiedi all'utente di inserire un comando
    command = codecs.encode(command, encoding)  # Codifica il comando utilizzando la codifica specificata
    client_socket.send(command)
    print('Comando Inviato')
    output = client_socket.recv(4096)
    output = codecs.decode(output, encoding)  # Decodifica l'output utilizzando la codifica specificata
    print(f"Output: {output}")


client_socket.close()  # Chiudi la connessione
