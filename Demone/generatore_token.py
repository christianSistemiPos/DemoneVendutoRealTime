import base64
import hashlib
import requests
import json
import sys
import subprocess



def genera_token_automatico():
    try:
        fernet = Fernet(open(sys.path[0] +"/Assistenza/vrt.key", "rb").read())
    except Exception as ex:
        print("ERRORE ERRRORE ERRORE")
        print("Controllare la presenza di vrt.key nella cartella Assistenza!")
        sys.exit(-1)
    with open(sys.path[0] +'/config.json', 'rb') as f:
        data = f.read()
    decrypted_data = fernet.decrypt(data)
    with open(sys.path[0] + "/config.json", "w") as config:
        config.write(decrypted_data.decode())
    print("Lettura Configurazione..")
    try:
        with open(sys.path[0] +"./config.json") as config:
            configuration = json.load(config)
    except Exception as ex:
        print(ex)
        sys.exit(-1)
    print("Ok")
    print("Generatore token di autenticazione per servizi uakari..")
    print("Inserire username")
    username = "utente"
    print("Inserire password")
    password = "utente2020"
    password = hashlib.md5(password.encode('utf-8'))
    print(f"Password criptata: {str(password.hexdigest())}")
    response = requests.post(f"{configuration['applicazione']['server']}/API/Users/Login",
                             data={
                                 'Username': username,
                                 'Password': password.hexdigest()
                             }
                             )
    print("Comunicazione avvenuta..")
    print("Risposta del web server:")
    print(response.json())
    print("Salvataggio token autenticazione nel file config.json")
    configuration["in"]["API"]["token_autorizzazione"] = response.json()["Token"]
    with open("./config.json", "w") as config:
        json.dump(configuration, config)

    print("Inizio crittografia file configurazione...")
    print("Assicurarsi di aver inserito tutti i dati correttamente..")
    print("Inizio cifratura..")
    with open('./config.json', 'rb') as f:
        data = f.read()
    encrypted_data = base64.b64encode(data)
    with open('./config.json', 'wb') as f:
        f.write(encrypted_data)

if __name__ == "__main__":

    print("Lettura Configurazione..")
    try:
        with open("../Installazione/config.json") as config:
            configuration = json.load(config)
    except Exception as ex:
        print(ex)
        sys.exit(-1)
    print("Ok")
    print("Generatore token di autenticazione per servizi uakari..")
    print("Inserire username")
    username = input()
    print("Inserire password")
    password = input()
    password = hashlib.md5(password.encode('utf-8'))
    print(f"Password criptata: {str(password.hexdigest())}")
    response = requests.post(f"{configuration['applicazione']['server']}/API/Users/Login",
                             data={
                                 'Username': username,
                                 'Password': password.hexdigest()
                             }
                             )
    print("Comunicazione avvenuta..")
    print("Risposta del web server:")
    print(response.json())
    print("Salvataggio token autenticazione nel file config.json")
    configuration["in"]["API"]["token_autorizzazione"] = response.json()["Token"]
    with open("config.json","w") as config:
        json.dump(configuration, config)

    print("Inizio crittografia file configurazione...")
    print("Assicurarsi di aver inserito tutti i dati correttamente..")
    print("Inizio cifratura..")
    
    with open('./config.json', 'rb') as f:
        data = f.read()
    encrypted_data = base64.b64encode(data)
    with open('./config.json', 'wb') as f:
        f.write(encrypted_data)
    print("Fine. :)")
    
    print("Premere invio per chiudere..")
    input = input()
