import base64
import sys
import os
sys.path.append(os.getcwd())
if __name__ == "__main__":
    print("Christian SistemiPOS :)")
    print("Decriptatore file di configurazione")
    print("Lettura chiave di cifratura:")
    with open('C:\SistemiPos\VendutoRealTime\Demone\config.json', 'rb') as f:
        data = f.read()
    decrypted_data = base64.b64decode(data).decode('utf-8')
    with open('C:\SistemiPos\VendutoRealTime\Demone\config.json', 'w') as f:
        f.write(decrypted_data)

    print("Fine. :)")