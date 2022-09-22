import base64
import sys
import os
sys.path.append(os.getcwd())

if __name__ == "__main__":
    print("Christian SistemiPOS :)")
    print("Inizio crittografia file configurazione...")
    print("Assicurarsi di aver inserito tutti i dati correttamente..")
    print("Inizio cifratura..")
    with open('C:\SistemiPos\VendutoRealTime\Demone\config.json', 'rb') as f:
        data = f.read()
    encrypted_data = base64.b64encode(data)
    with open('C:\SistemiPos\VendutoRealTime\Demone\config.json', 'wb') as f:
        f.write(encrypted_data)
    print("Fine. :)")