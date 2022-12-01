
from http.server import ThreadingHTTPServer
import sys,os
import uuid

sys.path.append(os.getcwd())
sys.path.append("C:\SistemiPos\VendutoRealTime\Demone")
from API.Model.Anomalia import TipoAnomalia
import time
import logging
from Database import db
from Database.Licenza import TableLicenza as Licenza, licenze_db
from Database.Reparto import TableReparto as Reparto
from Database.Pagamento import TablePagamento as Pagamento
from Database.Negozio import TableNegozio as Negozio
from Database.Cassa import TableCassa as Cassa
from Database.Anomalia import TableAnomalia as Anomalia
from config import configuration
from pony.orm import *
from API.API import API
import json
import mysql.connector
from API.Model.Negozio import Negozio as ModelNegozio
from API.Model.Reparto import Reparto as ModelReparto
from API.Model.Cassa import Cassa as ModelCassa
import os
from datetime import datetime
import sys
sys.path.append("./API")
sys.path.append("./API/Model")
sys.path.append("./Database")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


logging.basicConfig(filename='demone.log',
                    level=logging.DEBUG, filemode='w')

db.generate_mapping(create_tables=True)

versione_demone = "1.1 stabile"
if __name__ == "__main__":
    while True:
        id_cliente=""
        logging.info("Christian SistemiPOS :)")
        logging.info("Chiamata di verifica licenza..")
        with db_session:
            licenza = Licenza.select(lambda licenza: licenza.id_licenza==configuration["applicazione"]["licenza"])
            if not licenza:
                logging.info("Licenza non valida!")
                sys.exit(-1)
            id_cliente = list(licenza)[0].id_cliente
        logging.info("OK.")
            
        # Utilizzo Interfaccia API
        if configuration["applicazione"]["funzionamento"] == "API":
            from generatore_token import genera_token_automatico
            logging.info("Inizio comunicazione con API Uakari..")
            logging.info("Caricamento Api..")
            try:
                api = API(web=True, token_autenticazione=configuration["in"]["API"]
                            ["token_autorizzazione"], url_server=configuration["applicazione"]["server"])
            except Exception as ex:
                logging.exception(ex)
                sys.exit(-1)
            logging.info("Ok.")
            logging.info("Inizio controllo token di autenticazione uakari..")
            if not(api.check_connection()):
                logging.info(
                    "Autenticazione fallita..\n Creazione nuovo token..")
                genera_token_automatico()
                logging.info(
                    "al prossimo riavvio partira` l'esecuzione Normalmente.")
                sys.exit(0)

        # Utilizzo Interfaccia DB
        if configuration["applicazione"]["funzionamento"] == "DB":
            logging.info("Inizio comunicazione con Uakari..")
            try:
                api = API(database_connection_string=(
                    f"driver={{ODBC Driver 17 for SQL Server}};server={configuration['in']['database']['db_address']};uid={configuration['in']['database']['db_username']};pwd={configuration['in']['database']['db_password']};database={configuration['in']['database']['db_name']};"))
            except Exception as ex:
                logging.exception(ex)
                sys.exit(1)
            logging.info("Ok.")
            logging.info("Controllo connessione con database Uakari..")
            if not(api.check_connection()):
                raise Exception("Connessione non disponibile")
            logging.info("Ok.")

        logging.info("Caricamento modello Negozio..")
        try:
            local_negozio = ModelNegozio(id_negozio=configuration["applicazione"]["codice_negozio"],
                                            nome_negozio=configuration["applicazione"]["nome"],
                                            id_cliente=id_cliente
                                            )
        except Exception as ex:
            logging.exception(ex)
            sys.exit(1)
        logging.info("Ok.")

        logging.info("Chiamata a Uakari, ritorno configurazione casse..")
        try:
            local_negozio = api.get_pos(local_negozio)
        except Exception as ex:
            logging.exception(ex)
        logging.info("Ok.")

        logging.info("Chiamata a Uakari, ritorno scontrini per casse..")
        try:
            local_negozio = api.get_valorizzazione_casse(negozio=local_negozio)
        except Exception as ex:
            logging.exception(ex)
        logging.info("Ok.")
        
        with db_session:
            # Cancellazione dati precedente iterazione
            Reparto.select(lambda _reparto: _reparto.id_negozio == local_negozio.id_negozio
                            and _reparto.id_cliente == local_negozio.id_cliente).delete()
            
            Cassa.select(lambda _cassa: _cassa.id_negozio == local_negozio.id_negozio
                            and _cassa.id_cliente == local_negozio.id_cliente).delete()
            
            Pagamento.select(lambda _pagamento: _pagamento.id_negozio == local_negozio.id_negozio
                                    and _pagamento.id_cliente == local_negozio.id_cliente).delete()
            
            Anomalia.select(lambda _anomalia: _anomalia.id_negozio == local_negozio.id_negozio
                                    and _anomalia.id_cliente == local_negozio.id_cliente).delete()
        
        with db_session:
            db_negozio = Negozio.select(lambda _negozio: _negozio.id_negozio == local_negozio.id_negozio
                                        and _negozio.id_cliente == local_negozio.id_cliente).first()
            if not db_negozio:
                db_negozio = Negozio(id_negozio=local_negozio.id_negozio,
                                    id_cliente=local_negozio.id_cliente,
                                    nome_negozio=local_negozio.nome_negozio,
                                    ultimo_aggiornamento=datetime.now(),
                                    chiuso=False,
                                    livello_max_fidelity=10
                                    )
            
            for cassa in local_negozio.casse:
                _cassa_db = Cassa(id_negozio=local_negozio.id_negozio,
                                    id_cassa=cassa.id_cassa,
                                    id_cliente=local_negozio.id_cliente,
                                    numero_scontrini=cassa.numero_scontrini,
                                    numero_scontrini_fidelity=cassa.numero_scontrini_fidelity,
                                    totale=cassa.totale
                                    )

                # Aggiornamento Reparti

                # Se si usano le api, i reparti ancora non sono gestiti.. i reparti sono hard-coded
                if configuration["applicazione"]["funzionamento"] == "API":
                    with open("reparti.json", "r") as _reparti:
                        reparti = json.load(_reparti)

                for reparto in cassa.incasso_per_reparto:
                    if configuration["applicazione"]["funzionamento"] == "API":
                        try:
                            reparto.nome = list(filter(
                                lambda _reparto: _reparto["rep_cod"] == reparto.codice, reparti["RECORDS"]))[0]['rep_dsa']
                        except Exception as ex:
                            logging.exception(ex)
                            reparto.nome = "Sconosciuto"

                    _reparto_db = Reparto(id_negozio=local_negozio.id_negozio,
                                            id_cliente=local_negozio.id_cliente,
                                            id_cassa=cassa.id_cassa,
                                            id_reparto=reparto.codice,
                                            nome=reparto.nome,
                                            incasso=reparto.incasso,
                                            presenza=reparto.presenza
                                            )

                # Aggiornamento Pagamenti
                
                for pagamento in cassa.incasso_per_tipo_pagamento:
                    
                    _pagamento_db = Pagamento(
                        id_cassa=_cassa_db.id_cassa,
                        id_cliente=local_negozio.id_cliente,
                        id_negozio=local_negozio.id_negozio,
                        tipo_pagamento=pagamento.tipo_pagamento,
                        incasso=pagamento.incasso
                    )
                
                # Prendo threshold fidelity
                threshold = db_negozio.livello_max_fidelity
                # Aggiornamento Anomalie
                for anomalia in cassa.anomalie:
                    # Filtro per le fidelity 
                    if anomalia.tipo_anomalia.value == "Fidelity":
                        nr_carta = anomalia.descrizione_anomalia.split(";")[0]
                        threshold_anomalia = int(anomalia.descrizione_anomalia.split(";")[1])
                        if int(threshold_anomalia) <= int(threshold):
                            continue
                        anomalia.descrizione_anomalia = f"La card fidelity Nr. {nr_carta} e` stata scansionata in cassa per {threshold_anomalia} volte, eccedendo il limite massimo giornaliero."
                    _ = Anomalia(
                            id_cassa=cassa.id_cassa,
                            id_cliente=local_negozio.id_cliente,
                            id_negozio=local_negozio.id_negozio,
                            tipo_anomalia=anomalia.tipo_anomalia.value,
                            ora_anomalia=anomalia.ora_anomalia,
                            operatore = anomalia.operatore,
                            descrizione_anomalia = anomalia.descrizione_anomalia,
                            id_anomalia=str(uuid.uuid4())
                        )
            db_negozio.ultimo_aggiornamento = datetime.now()
            db_negozio.versione_demone=versione_demone
        time.sleep(180)