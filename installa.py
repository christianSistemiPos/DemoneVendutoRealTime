import shutil
import os 
if __name__ == '__main__':
    print("Installazione programma venduto real time")
    for (index,file) in zip(range(len(os.listdir("C:\SistemiPos\VendutoRealTime/PDVVRT"))),os.listdir("C:\SistemiPos\VendutoRealTime/PDVVRT")):
        print(f"{index}) {file}")
    gruppo=input(f"Selezione Gruppo: ")
    gruppi = os.listdir("C:\SistemiPos\VendutoRealTime/PDVVRT")
    for (index,file) in zip(range(len(os.listdir("C:\SistemiPos\VendutoRealTime/PDVVRT"))),os.listdir(f"C:\SistemiPos\VendutoRealTime/PDVVRT/{gruppi[int(gruppo)]}")):
        print(f"{index}) {file}")
    negozi = os.listdir(f"C:\SistemiPos\VendutoRealTime/PDVVRT/{gruppi[int(gruppo)]}")
    negozio=input(f"Selezione Negozio: ")
    shutil.copyfile(f"C:\SistemiPos\VendutoRealTime/PDVVRT/{gruppi[int(gruppo)]}/{negozi[int(negozio)]}","C:\SistemiPos\VendutoRealTime\Demone/config.json")