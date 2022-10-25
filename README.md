# VendutoRealTime 
I PATH VANNO RISPETTATI ALTRIMENTI SO CAZZI AMARI.

COMPILARE IL FOGLIO GOOGLE PRIMA DI QUALUNQUE COSA, PERCHE' SI.
https://docs.google.com/spreadsheets/d/1j1DrHwa-U1DZaOuCpIPD5Rmj_Cx0439ynaySWLOOWlU/edit?usp=sharing

Ora siamo alla versione 1.1 STABILE

### Fase Preliminare, aggiungere file di configurazione nel registro configurazioni.

1) Aprire PDVVRT
2) Creare una cartella con il nome di riferimento per i negozi oppure usarne una gia' presente
3) Creare un file di configurazione nel formato xxxx_config.json dove xxxx sta per il codice del negozio
        Es. 0001_config.json
4) Seguire il file template_config.json per l'inserimento dei dati specifici al negozio
    - applicazione->codice_negozio 
        CODICE DEL NEGOZIO
    - applicazione->licenza 
        UUID DELLA LICENZA NEL DB LICENZE
    - applicazione->nome 
        NOME DEL PUNTO VENDITA
    - in->database 
        CONNECTION PROPERTIES DB UAKARI
    - out->database 
        CONNECTION PROPERTIES DB NOSTRO

### Installazione sul PDV

1) Creare sul pc del punto vendita una cartella al path C:\\sistemipos\
2) Trasferire le cartelle bin e PDVVRT in questa cartella
3) Trasferire git-portable.exe sotto C:\\
4) Avviare git-portable.exe e modificare il path di installazione in C:\\git
5) Aprire un terminale e incollare un istruzione per volta
    ```batch
    cd C:\\sistemipos
    C:\\git\bin\git clone https://github.com/christianSistemiPos/DemoneVendutoRealTime.git VendutoRealTime
    ```
6) Portarsi sollo C:\\sistemipos\VendutoRealTime
7) Lanciare RunMe.bat
8) Installare build tools e connector
...
9) Quando compare la selezione del punto vendita seguire i numeri, occhio che la numerazione parte da 0.
...
10) Quando si chiude il batch il servizio é gia' creato e pronto per essere avviato
11) Cancellare la cartella PDVVRT
12) Dopo che si lancia il servizio, in C:\\sistemipos\VendutoRealTime\Demone ci sono i log che produce il servizio
13) in C:\\sistemipos\VendutoRealTime\bin\demone.log c'é il log interno allo script

### Cosa devo fare per modificare il file config.json
- Il file config.json che ora si troverá in C:\\sistemipos\VendutoRealTime\Demone, in versione criptata, per essere modificato dovrá essere prima dectiptato con il batch in C:\\sistemipos\VendutoRealTime\Assistenza\, ASSICURARSI CHE IL SERVIZIO SIA SPENTO.
- Si modifica..
- Poi si cripta nuovamente con l'altro batch in C:\\sistemipos\VendutoRealTime\Assistenza\

