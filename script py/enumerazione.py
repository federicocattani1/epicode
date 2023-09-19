import http.client

ip_target = "192.168.50.101"
port = 80
metodi = ["GET", "OPTIONS", "POST", "HEAD", "TRACE", "DELETE", "PUT"]

for metodo in metodi 
      try:
            conn = http.client.HTTPConnection(ip_target, port)
            conn.request(metodo, "/")
            response = conn.getresponse()
            if response.status < 400:
                  print("il metodo {metodo} è abilitato")

            else
                    print("il metodo {metodo} non è abilitato")
      except ConnectionRefusedError:
                  print("connnessione rifiutata")
      except http.client.HTTPException:
                  print("Errore durante la richiesta al server")
        
        conn.close