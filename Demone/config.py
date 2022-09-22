import json
import sys
import base64
sys.path.append("C:\SistemiPos\VendutoRealTime\Demone")

print("Lettura Configurazione..")
with open('C:\SistemiPos\VendutoRealTime\Demone\config.json', 'rb') as f:
    data = f.read()
try:
    decrypted_data = base64.b64decode(data).decode('utf-8')
except Exception as ex:
    print("Errore Errore Errore")
    print("Assicurarsi che config.json sia criptato")
    key = input()
    sys.exit(-1)
configuration = json.loads(decrypted_data)
print("Ok")