import socket

def scan_ports(target, port_a, port_b):
    
    for port in range(port_a, port_b + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port} is open")
        
        sock.close()

target = input("Inserisci il target: ")
port_a = int(input("Inserisci il numero di porta iniziale: "))
port_b = int(input("Inserisci il numero di porta finale: "))

scan_ports(target, port_a, port_b)
